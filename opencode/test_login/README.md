# 自动登录脚本使用说明

## 📋 项目结构
```
C:\Users\iflytek\Desktop\code\
├── main.py              # 主程序入口
├── login_handler.py     # 登录处理核心逻辑
├── config.py            # 配置文件
├── logger.py            # 日志系统
├── requirements.txt     # 依赖包列表
└── auto_login.log       # 运行日志（自动生成）
```

## 🚀 快速开始

### 1. 运行脚本
```bash
cd C:\Users\iflytek\Desktop\code
python main.py
```

### 2. 功能特点
- ✅ 自动测试两个账号登录
- ✅ 智能元素定位和等待
- ✅ 详细日志记录
- ✅ 登录结果截图
- ✅ 错误处理和重试机制
- ✅ 忽略HTTPS证书错误

## ⚙️ 配置说明

### 账号配置 (config.py)
```python
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
```

### 元素选择器 (config.py)
脚本使用智能选择器自动识别登录表单元素：
- **用户名输入框**: `input[type="text"], input[name="username"], ...`
- **密码输入框**: `input[type="password"], input[name="password"], ...`
- **登录按钮**: `button[type="submit"], button:has-text("登录"), ...`

## 📊 输出结果

### 1. 控制台输出
- 实时显示登录进度
- 成功/失败状态
- 详细错误信息

### 2. 日志文件
- 完整运行日志：`auto_login.log`
- 支持日志轮转，最大10MB

### 3. 截图文件
- `login_result_super.png` - super账号登录结果
- `login_result_admin.png` - admin账号登录结果

## 🔧 高级配置

### 浏览器设置
```python
BROWSER_CONFIG = {
    'headless': False,    # 是否无头模式
    'window_size': {'width': 1366, 'height': 768},
    'ignore_https_errors': True  # 忽略HTTPS证书错误
}
```

### 超时设置
```python
LOGIN_CONFIG = {
    'login_timeout': 30,      # 登录超时时间
    'page_wait_time': 2000,   # 页面等待时间
    'retry_count': 2          # 重试次数
}
```

## 🛠️ 故障排除

### 常见问题

1. **元素定位失败**
   - 检查网站是否使用了特殊的输入框结构
   - 使用浏览器开发者工具查看实际元素选择器
   - 修改config.py中的选择器配置

2. **登录超时**
   - 增加`login_timeout`值
   - 检查网络连接
   - 确认网站响应速度

3. **证书错误**
   - 脚本已配置忽略证书错误
   - 如仍有问题，检查系统时间是否正确

### 调试模式
将`BROWSER_CONFIG['headless']`设为`False`可显示浏览器窗口，便于调试。

## 📞 技术支持
如遇到问题，请检查日志文件`auto_login.log`获取详细信息。