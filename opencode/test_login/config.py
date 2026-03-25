# 登录配置
LOGIN_CONFIG = {
    # 登录页面URL
    'login_url': 'https://10.54.69.234:30018/',
    
    # 元素选择器 (基于常见登录页面结构)
    'username_selector': 'input[type="text"], input[name="username"], input[id="username"], input[placeholder*="账号"], input[placeholder*="用户"]',
    
    'password_selector': 'input[type="password"], input[name="password"], input[id="password"], input[placeholder*="密码"]',
    
    'login_button_selector': 'button[type="submit"], input[type="submit"], button:has-text("登录"), .login-btn, #login-btn',
    
    # 登录超时时间 (秒)
    'login_timeout': 30,
    
    # 页面加载等待时间 (毫秒)
    'page_wait_time': 2000,
    
    # 重试次数
    'retry_count': 2
}

# 账号配置
ACCOUNTS = [
    {
        'username': 'super',
        'password': 'GNsz135!#%',
        'description': '超级管理员账号'
    },
    {
        'username': 'admin', 
        'password': 'GNsz135!#%ad',
        'description': '管理员账号'
    }
]

# 浏览器配置
BROWSER_CONFIG = {
    'headless': False,  # 是否无头模式 (调试用False)
    'window_size': {'width': 1366, 'height': 768},
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'ignore_https_errors': True,  # 忽略HTTPS证书错误
    'accept_downloads': True
}

# 日志配置
LOG_CONFIG = {
    'log_level': 'INFO',  # DEBUG, INFO, WARNING, ERROR
    'log_file': 'auto_login.log',
    'max_file_size': 10 * 1024 * 1024,  # 10MB
    'backup_count': 5
}