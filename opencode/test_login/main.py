#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动登录脚本 - 主程序
功能：自动测试多个账号登录指定网站
作者：Auto Login Script
版本：1.0
"""

import time
import sys
from login_handler import LoginHandler
from config import ACCOUNTS
from logger import setup_logger

logger = setup_logger(__name__)

def main():
    """主函数"""
    logger.info("🚀 自动登录脚本启动")
    
    # 创建登录处理器
    login_handler = LoginHandler()
    
    try:
        # 初始化浏览器
        if not login_handler.setup_browser():
            logger.error("❌ 浏览器初始化失败，脚本退出")
            return 1
        
        logger.info(f"📋 开始测试 {len(ACCOUNTS)} 个账号登录")
        
        # 测试结果统计
        success_count = 0
        fail_count = 0
        results = []
        
        # 遍历测试每个账号
        for i, account in enumerate(ACCOUNTS, 1):
            logger.info(f"\n🔐 正在测试第 {i}/{len(ACCOUNTS)} 个账号: {account['description']} ({account['username']})")
            
            try:
                # 执行登录
                login_success = login_handler.login_with_credentials(
                    account['username'], 
                    account['password']
                )
                
                # 截图保存结果
                screenshot_filename = f"login_result_{account['username']}.png"
                login_handler.take_screenshot(screenshot_filename)
                
                # 记录结果
                result = {
                    'username': account['username'],
                    'description': account['description'],
                    'success': login_success,
                    'screenshot': screenshot_filename
                }
                results.append(result)
                
                if login_success:
                    success_count += 1
                    logger.info(f"✅ {account['description']} 登录成功")
                else:
                    fail_count += 1
                    logger.warning(f"❌ {account['description']} 登录失败")
                
                # 如果不是最后一个账号，先退出登录再测试下一个
                if i < len(ACCOUNTS):
                    logger.info("执行退出登录操作...")
                    logout_success = login_handler.logout()
                    if logout_success:
                        logger.info("退出登录成功，等待页面加载...")
                        # 等待登录页面重新加载
                        login_handler.wait_for_login_page(timeout=5)
                    else:
                        logger.warning("退出登录可能失败，继续测试下一个账号")
                    logger.info("等待2秒后测试下一个账号...")
                    time.sleep(2)
                
            except Exception as e:
                logger.error(f"测试账号 {account['username']} 时出错: {e}")
                fail_count += 1
                results.append({
                    'username': account['username'],
                    'description': account['description'],
                    'success': False,
                    'error': str(e)
                })
        
        # 输出测试报告
        logger.info("\n" + "="*50)
        logger.info("📊 登录测试报告")
        logger.info("="*50)
        logger.info(f"总测试账号数: {len(ACCOUNTS)}")
        logger.info(f"✅ 成功: {success_count}")
        logger.info(f"❌ 失败: {fail_count}")
        logger.info(f"成功率: {success_count/len(ACCOUNTS)*100:.1f}%")
        
        logger.info("\n详细结果:")
        for result in results:
            status = "✅ 成功" if result['success'] else "❌ 失败"
            logger.info(f"  {result['description']} ({result['username']}): {status}")
            if 'screenshot' in result:
                logger.info(f"    截图: {result['screenshot']}")
        
        return 0 if success_count == len(ACCOUNTS) else 1
        
    except KeyboardInterrupt:
        logger.info("\n⏹️  用户中断操作")
        return 130
        
    except Exception as e:
        logger.error(f"❌ 脚本执行出错: {e}")
        return 1
        
    finally:
        # 清理资源
        if login_handler:
            login_handler.cleanup()
        logger.info("\n🏁 自动登录脚本执行完成")

if __name__ == "__main__":
    sys.exit(main())