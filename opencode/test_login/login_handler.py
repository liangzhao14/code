from playwright.sync_api import sync_playwright, Page, Browser
import time
from config import LOGIN_CONFIG
from logger import setup_logger
from typing import Optional

logger = setup_logger(__name__)

class LoginHandler:
    def __init__(self):
        self.playwright = None
        self.browser: Optional[Browser] = None
        self.page: Optional[Page] = None
        
    def setup_browser(self):
        """初始化浏览器"""
        try:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(
                headless=False,  # 显示浏览器窗口便于调试
                args=['--ignore-certificate-errors']  # 忽略证书错误
            )
            self.page = self.browser.new_page()
            logger.info("浏览器初始化成功")
            return True
        except Exception as e:
            logger.error(f"浏览器初始化失败: {e}")
            return False
    
    def wait_for_login_page(self, timeout=10):
        """智能等待登录页面加载完成"""
        try:
            logger.info("等待登录页面加载...")
            
            # 等待页面加载指示器
            indicators = [
                'input[type="text"], input[name="username"], input[id="username"]',
                'input[type="password"], input[name="password"], input[id="password"]',
                'button[type="submit"], input[type="submit"]',
                '.login-form', '.login-container', '.login-box',
                '[class*="login"]', '[id*="login"]'
            ]
            
            for indicator in indicators:
                try:
                    if self.page:
                        self.page.wait_for_selector(indicator, timeout=timeout*1000)
                        logger.info(f"登录页面加载完成，发现元素: {indicator}")
                        return True
                except:
                    continue
            
            # 检查页面是否已跳转（可能已登录）
            if self.page and self.page.url != LOGIN_CONFIG['login_url']:
                logger.info(f"页面已跳转: {self.page.url}")
                return True
                
            logger.warning("登录页面加载超时")
            return False
            
        except Exception as e:
            logger.error(f"等待登录页面出错: {e}")
            return False
    
    def login_with_credentials(self, username, password):
        """使用指定账号密码登录"""
        try:
            logger.info(f"开始登录 - 账号: {username}")
            
            if not self.page:
                logger.error("页面未初始化")
                return False
            
            # 访问登录页面
            logger.info(f"访问登录页面: {LOGIN_CONFIG['login_url']}")
            self.page.goto(LOGIN_CONFIG['login_url'], wait_until='networkidle')
            
            # 等待页面加载
            self.wait_for_login_page()
            
            # 填充账号密码
            logger.info("填充账号密码...")
            self.page.fill(LOGIN_CONFIG['username_selector'], username)
            self.page.fill(LOGIN_CONFIG['password_selector'], password)
            
            # 点击登录按钮
            logger.info("点击登录按钮...")
            self.page.click(LOGIN_CONFIG['login_button_selector'])
            
            # 等待登录结果
            self.page.wait_for_timeout(3000)
            
            # 检查登录是否成功
            if self.check_login_success():
                logger.info(f"✅ 账号 {username} 登录成功")
                return True
            else:
                logger.warning(f"❌ 账号 {username} 登录可能失败")
                return False
                
        except Exception as e:
            logger.error(f"登录过程中出错 - 账号 {username}: {e}")
            return False
    
    def logout(self):
        """退出登录"""
        try:
            logger.info("正在执行退出登录...")
            
            if not self.page:
                logger.error("页面未初始化，无法退出登录")
                return False
            
            # 尝试点击右上角头像或用户菜单 - 增强版
            user_menu_selectors = [
                'img[alt*="avatar"], img[alt*="user"]',
                '[class*="avatar"], [class*="user-avatar"]',
                '[class*="user-menu"], [class*="profile-menu"]',
                'button:has-text("用户"), button:has-text("账号")',
                '[data-toggle*="dropdown"], [class*="dropdown-toggle"]',
                '.el-avatar',  # Element UI
                '.ant-avatar',  # Ant Design
                '.user-info',
                '.header-user',
                '.navbar-right .user',
                '[class*="header"] [class*="user"]',
                '.right-menu .avatar-container'  # 常见后台管理系统
            ]
            
            # 查找用户菜单
            user_menu_found = False
            clicked_element = None
            
            for selector in user_menu_selectors:
                try:
                    if self.page:
                        elements = self.page.query_selector_all(selector)
                        if elements:
                            # 检查元素是否可见
                            for element in elements:
                                if element.is_visible():
                                    logger.info(f"找到可见的用户菜单元素: {selector}")
                                    element.click()
                                    clicked_element = element
                                    self.page.wait_for_timeout(1500)
                                    user_menu_found = True
                                    break
                            if user_menu_found:
                                break
                except Exception as e:
                    logger.debug(f"尝试选择器 {selector} 失败: {e}")
                    continue
            
            if not user_menu_found:
                logger.warning("未找到用户菜单，尝试直接查找退出登录按钮")
            
            # 查找退出登录按钮 - 增强版，等待下拉菜单出现
            logout_selectors = [
                'a:has-text("退出"), button:has-text("退出")',
                'a:has-text("登出"), button:has-text("登出")',
                'a:has-text("注销"), button:has-text("注销")',
                'a:has-text("Logout"), button:has-text("Logout")',
                '[class*="logout"], [id*="logout"]',
                'a[href*="logout"], button[onclick*="logout"]',
                '.dropdown-menu a:has-text("退出")',
                '.el-dropdown-menu a:has-text("退出")',  # Element UI
                '.ant-dropdown-menu a:has-text("退出")',  # Ant Design
                '.user-dropdown a:has-text("退出")',
                '.menu-item:has-text("退出")',
                'li:has-text("退出")',
                '.logout-btn',
                '[title*="退出"]', 
                '[aria-label*="退出"]'
            ]
            
            logout_found = False
            
            # 等待下拉菜单出现
            self.page.wait_for_timeout(1000)
            
            for selector in logout_selectors:
                try:
                    if self.page:
                        # 先等待元素出现
                        try:
                            self.page.wait_for_selector(selector, timeout=3000)
                        except:
                            continue
                            
                        elements = self.page.query_selector_all(selector)
                        if elements:
                            # 找到可见的退出按钮
                            for element in elements:
                                if element.is_visible():
                                    logger.info(f"点击退出登录: {selector}")
                                    element.click()
                                    self.page.wait_for_timeout(2000)
                                    logout_found = True
                                    break
                            if logout_found:
                                break
                except Exception as e:
                    logger.debug(f"尝试退出选择器 {selector} 失败: {e}")
                    continue
            
            # 如果还是找不到，尝试JavaScript点击
            if not logout_found:
                logger.info("尝试使用JavaScript执行退出登录...")
                try:
                    # 查找所有包含退出文本的元素
                    logout_elements = self.page.evaluate("""
                        () => {
                            const allElements = document.querySelectorAll('*');
                            const logoutElements = [];
                            for (let el of allElements) {
                                if (el.textContent && el.textContent.includes('退出') && el.onclick) {
                                    logoutElements.push(el);
                                }
                            }
                            return logoutElements.length;
                        }
                    """)
                    
                    if logout_elements > 0:
                        self.page.evaluate("""
                            () => {
                                const allElements = document.querySelectorAll('*');
                                for (let el of allElements) {
                                    if (el.textContent && el.textContent.includes('退出') && el.onclick) {
                                        el.click();
                                        break;
                                    }
                                }
                            }
                        """)
                        self.page.wait_for_timeout(2000)
                        logout_found = True
                        logger.info("JavaScript点击退出登录成功")
                except Exception as e:
                    logger.debug(f"JavaScript点击失败: {e}")
            
            if logout_found:
                logger.info("✅ 退出登录成功")
                # 智能处理退出后的确认对话框
                self.handle_logout_confirmation()
                # 等待页面回到登录页
                time.sleep(1)
                return True
            else:
                logger.warning("❌ 未找到退出登录按钮")
                # 作为备选方案，直接访问登录页面
                try:
                    self.page.goto(LOGIN_CONFIG['login_url'])
                    logger.info("已直接导航到登录页面")
                    return True
                except:
                    return False
                
        except Exception as e:
            logger.error(f"退出登录时出错: {e}")
            return False
    
    def handle_logout_confirmation(self):
        """智能处理退出登录后的确认对话框"""
        try:
            logger.info("智能检测退出确认对话框...")
            
            # 常见的确认对话框选择器
            confirmation_selectors = [
                # 确认按钮
                'button:has-text("确定"), button:has-text("确认")',
                'button:has-text("OK"), button:has-text("Ok")',
                '.el-message-box__wrapper button:has-text("确定")',  # Element UI
                '.ant-modal-confirm .ant-btn-primary',  # Ant Design
                '.confirm-btn, .ok-btn, .yes-btn',
                'button[class*="confirm"]', 
                '.modal-footer button:has-text("确定")',
                '.dialog-footer button:has-text("确定")',
                # 取消按钮（有时需要点击取消）
                'button:has-text("取消"), button:has-text("Cancel")',
                '.el-message-box__wrapper button:has-text("取消")',
                '.ant-modal-confirm .ant-btn-default'
            ]
            
            # 等待确认对话框出现
            time.sleep(0.5)
            
            dialog_found = False
            for selector in confirmation_selectors:
                try:
                    if not self.page:
                        continue
                        
                    # 等待元素出现（最多等待3秒）
                    self.page.wait_for_selector(selector, timeout=3000)
                    elements = self.page.query_selector_all(selector)
                    
                    for element in elements:
                        if element.is_visible():
                            button_text = element.text_content()
                            if button_text:
                                button_text = button_text.strip()
                                logger.info(f"发现确认对话框按钮: {button_text}")
                                
                                # 智能判断点击哪个按钮
                                if "确定" in button_text or "确认" in button_text or "OK" in button_text:
                                    logger.info(f"点击确认按钮: {button_text}")
                                    element.click()
                                    dialog_found = True
                                    break
                                elif "取消" in button_text or "Cancel" in button_text:
                                    # 有时需要点击取消，记录但不自动点击
                                    logger.info(f"发现取消按钮: {button_text}，如需点击请手动确认")
                                    # 可以选择不点击取消，继续寻找确定按钮
                                    continue
                    
                    if dialog_found:
                        break
                        
                except:
                    continue
            
            # 如果没有找到标准的确认对话框，检查是否有alert
            try:
                if self.page:
                    self.page.on("dialog", lambda dialog: dialog.accept())
                    logger.info("已设置自动接受alert对话框")
            except:
                pass
            
            # 等待确认操作完成
            if dialog_found:
                time.sleep(1)
                logger.info("✅ 确认对话框处理完成")
            else:
                logger.info("未检测到确认对话框，可能无需确认")
                
        except Exception as e:
            logger.debug(f"处理确认对话框时出错: {e}")
            # 不影响主流程，继续执行
    
    def check_login_success(self):
        """检查登录是否成功"""
        try:
            if not self.page:
                return False
                
            # 检查URL是否变化
            current_url = self.page.url
            if current_url != LOGIN_CONFIG['login_url']:
                logger.info(f"页面URL已变化: {current_url}")
                return True
            
            # 检查是否有错误提示
            error_elements = self.page.query_selector_all('.error, .alert-error, [class*="error"]')
            if error_elements:
                error_text = error_elements[0].text_content()
                logger.warning(f"发现错误提示: {error_text}")
                return False
            
            # 检查是否有登出按钮或用户信息
            logout_elements = self.page.query_selector_all('[class*="logout"], [class*="user"], [class*="profile"]')
            if logout_elements:
                logger.info("发现用户相关元素，登录可能成功")
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"检查登录状态时出错: {e}")
            return False
    
    def take_screenshot(self, filename):
        """截图保存"""
        try:
            if not self.page:
                logger.error("页面未初始化，无法截图")
                return False
            screenshot_path = f"C:\\Users\\iflytek\\Desktop\\code\\{filename}"
            self.page.screenshot(path=screenshot_path, full_page=True)
            logger.info(f"截图已保存: {screenshot_path}")
            return True
        except Exception as e:
            logger.error(f"截图失败: {e}")
            return False
    
    def cleanup(self):
        """清理资源"""
        try:
            if self.browser:
                self.browser.close()
            if self.playwright:
                self.playwright.stop()
            logger.info("浏览器资源已清理")
        except Exception as e:
            logger.error(f"清理资源时出错: {e}")

if __name__ == "__main__":
    # 测试登录处理器
    login_handler = LoginHandler()
    
    if login_handler.setup_browser():
        # 测试super账号
        login_handler.login_with_credentials("super", "GNsz135!#%")
        login_handler.take_screenshot("super_login_result.png")
        
        # 等待几秒后测试admin账号
        time.sleep(2)
        login_handler.page.goto(LOGIN_CONFIG['login_url'])
        login_handler.login_with_credentials("admin", "GNsz135!#%ad")
        login_handler.take_screenshot("admin_login_result.png")
        
        login_handler.cleanup()