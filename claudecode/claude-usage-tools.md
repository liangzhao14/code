# Claude Code 使用量查看工具

本机已安装两个 Claude Code 用量监控工具：**ccusage**（npm）和 **claude-monitor**（pip）。

---

## 1. ccusage（v18.0.10）

读取本地 Claude Code 会话日志，统计 token 用量和费用。

### 安装

```bash
npm install -g ccusage
```

### 基本命令

| 命令                | 说明         |
| ----------------- | ---------- |
| `ccusage`         | 默认按日显示用量报告 |
| `ccusage daily`   | 按日分组       |
| `ccusage weekly`  | 按周分组       |
| `ccusage monthly` | 按月分组       |
| `ccusage session` | 按会话分组      |
| `ccusage blocks`  | 按计费块分组     |

### 常用选项

| 选项                        | 说明                       |
| ------------------------- | ------------------------ |
| `-s, --since <YYYYMMDD>`  | 起始日期过滤                   |
| `-u, --until <YYYYMMDD>`  | 截止日期过滤                   |
| `-b, --breakdown`         | 显示各模型费用明细                |
| `-o, --order <desc\|asc>` | 排序方式（desc 最新在前，asc 最早在前） |
| `-j, --json`              | JSON 格式输出                |
| `-i, --instances`         | 按项目/实例分组显示               |
| `-p, --project <name>`    | 按项目名过滤                   |
| `-z, --timezone <tz>`     | 时区（如 `Asia/Shanghai`）    |
| `--compact`               | 紧凑模式，适合窄屏截图              |
| `-O, --offline`           | 离线模式，使用缓存定价数据            |

### 使用示例

```bash
# 查看每日用量
ccusage daily

# 查看本周用量，最新在前
ccusage daily --since 20260316 --order desc

# 查看某段时间内的用量，并显示模型明细
ccusage daily --since 20260301 --until 20260318 --breakdown

# 按月统计
ccusage monthly

# 查看各会话的用量
ccusage session

# 查看当前活跃的计费块及预估用量
ccusage blocks --active

# 查看最近 3 天的计费块
ccusage blocks --recent

# 按项目过滤
ccusage daily --project credit-card-manager

# JSON 输出并用 jq 处理
ccusage daily --json
ccusage daily --jq '.[] | select(.cost > 1)'

# 使用上海时区
ccusage daily --timezone Asia/Shanghai
```

### blocks 子命令专属选项

| 选项                             | 说明              |
| ------------------------------ | --------------- |
| `-a, --active`                 | 仅显示当前活跃计费块及预估   |
| `-r, --recent`                 | 显示最近 3 天的计费块    |
| `-t, --token-limit <num>`      | 设置 token 配额警告阈值 |
| `-n, --session-length <hours>` | 计费块时长，默认 5 小时   |

### session 子命令专属选项

| 选项                      | 说明            |
| ----------------------- | ------------- |
| `-i, --id <session_id>` | 查看指定会话 ID 的用量 |

---

## 2. claude-monitor（v3.1.0）

实时 TUI 监控面板，在终端中持续刷新显示 Claude 用量。

### 安装

```bash
pip install claude-monitor
```

### 基本命令

```bash
claude-monitor
```

### 常用选项

| 选项                                           | 说明                    |
| -------------------------------------------- | --------------------- |
| `--plan <pro\|max5\|max20\|custom>`          | 订阅计划类型                |
| `--view <realtime\|daily\|monthly\|session>` | 视图模式                  |
| `--theme <light\|dark\|classic\|auto>`       | 显示主题                  |
| `--timezone <tz>`                            | 时区（如 `Asia/Shanghai`） |
| `--time-format <12h\|24h>`                   | 时间格式                  |
| `--refresh-rate <seconds>`                   | 数据刷新间隔，默认 10 秒        |
| `--custom-limit-tokens <num>`                | 自定义计划的 token 上限       |
| `--reset-hour <0-23>`                        | 每日限额重置小时              |
| `--clear`                                    | 清除已保存的配置              |
| `--version`                                  | 显示版本号                 |
| `--debug`                                    | 开启调试日志                |

### 使用示例

```bash
# 默认实时监控
claude-monitor

# 指定 Max 5 计划，深色主题
claude-monitor --plan max5 --theme dark

# 按日视图查看，使用上海时区
claude-monitor --view daily --timezone Asia/Shanghai

# 按月视图
claude-monitor --view monthly

# 按会话视图
claude-monitor --view session

# 自定义 token 限额和刷新频率
claude-monitor --plan custom --custom-limit-tokens 500000 --refresh-rate 5

# 使用 24 小时制
claude-monitor --time-format 24h
```

---

## 两个工具的区别

| 对比项     | ccusage             | claude-monitor     |
| ------- | ------------------- | ------------------ |
| 类型      | CLI 报告工具            | 实时 TUI 监控面板        |
| 输出      | 静态表格/JSON           | 持续刷新的终端界面          |
| 适合场景    | 查看历史统计、导出数据         | 实时监控当前用量           |
| 日期过滤    | 支持（--since/--until） | 通过视图模式切换           |
| JSON 导出 | 支持                  | 不支持                |
| 计划感知    | 无                   | 支持（pro/max5/max20） |
