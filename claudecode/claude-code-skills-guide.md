# Claude Code Skills 精选 9 个极简教程

> 来源：微信公众号 HiddenState《🤳Skills极简教程，Claude Code只需这9个》（2026.03）
>
> 翻遍了官方和社区装了几十个 Skills，实践证明，最后真正反复在用的就这 9 个。

---

## 什么是 Skills？

你可以给 Claude Code 装各种"技能包"，装上之后一句话就能触发一整套工作流。**写一次，永久生效，不用反复复制粘贴 prompt。**

> Skills 遵循 Agent Skills 开放标准，不只 Claude Code 能用——Cursor、Codex、Gemini CLI 也认同样的格式。写一次，到处用。

---

## 9 个推荐 Skills

### Skill 01 · Superpowers

**社区最火的 Skills，没有之一。**

不是单个技能，而是一整套软件开发方法论——从规划、编码、调试到 Code Review 全覆盖。装上后 Claude Code 做事明显更有章法，不再东一榔头西一棒子。属于必装级别。

**覆盖场景：** 开发

---

### Skill 02 · PDF

能读取、合并、拆分、旋转、加水印、OCR 识别、填写 PDF 表单。日常处理合同、报告、论文，不用再开 Adobe。这是 claude.ai 网页版文档功能背后的同款能力。

**覆盖场景：** 开发 / 内容

---

### Skill 03 · Humanizer-zh

专门去除中文文本里的 AI 写作痕迹。基于一套 AI 写作特征识别规则，帮你把「此外」、「综上所述」这类 AI 味儿重的表达替换成更自然的人话。写公众号、写小红书、写报告怕被看出是 AI 写的，这个太实用了。

**覆盖场景：** 内容

---

### Skill 04 · Planning With Files

Manus 式的持久化项目规划。它会创建一个结构化的 Markdown 计划文件，Claude Code 每次启动都会读取，**跨 session 不丢进度**。做大项目最怕 AI 忘了上下文，这个直接解决。

**覆盖场景：** 开发

---

### Skill 05 · frontend-design

让 Claude Code 写出来的前端不再是「一看就是 AI 生成的」。内置一套设计规范，生成的网页、仪表盘都是生产级别的视觉质量。不需要懂设计，它帮你审美拉到及格线以上。

**覆盖场景：** 设计

---

### Skill 06 · Playwright

浏览器自动化神器。装上后 Claude Code 能打开网页、点击按钮、填写表单、截图——自动登录后台、批量操作、抓取数据全靠它。

**覆盖场景：** 自动化

---

### Skill 07 · code-review

不是普通的代码审查。**同时派出多个子 Agent，分别从代码质量、安全性、性能等维度并行审查**，每个发现都带置信度评分。比人工 Review 更全面也更快，适合团队和个人自查。

**覆盖场景：** 开发

---

### Skill 08 · Marketing Skills

这个不是给程序员用的——覆盖 SEO 优化、转化率分析、文案撰写、增长策略。非技术人员也能通过 Claude Code 做专业的营销分析。谁说 Claude Code 只能写代码？

**覆盖场景：** 营销

---

### Skill 09 · Skill Creator（压轴）

**这是用来创建新 Skill 的 Skill。** 描述你想要什么工作流，它帮你生成标准格式的 SKILL.md 文件，还能跑评测验证效果。等于授人以渔——上面 8 个不够用的话，自己造。

**覆盖场景：** 开发 / 自动化

---

## 安装方式

### 方式一：官方 Skills（推荐）

在 Claude Code 里输入以下命令：

```
/plugin install {名称}@claude-plugin-directory
```

例如安装 superpowers：

```
/plugin install superpowers@claude-plugin-directory
```

### 方式二：三方 Skills

去 GitHub 下载对应仓库，将文件放到项目的 `.claude/skills/` 目录下即可。

---

## 快速一览

| # | Skill 名称 | 核心能力 | 场景 |
|---|-----------|---------|------|
| 01 | Superpowers | 完整开发方法论（规划→编码→Review） | 开发 |
| 02 | PDF | 读取/合并/拆分/OCR/填表 | 开发/内容 |
| 03 | Humanizer-zh | 去除中文 AI 写作痕迹 | 内容 |
| 04 | Planning With Files | 持久化项目规划，跨 session 保存 | 开发 |
| 05 | frontend-design | 生产级前端视觉规范 | 设计 |
| 06 | Playwright | 浏览器自动化（点击/填表/截图） | 自动化 |
| 07 | code-review | 多 Agent 并行代码审查 | 开发 |
| 08 | Marketing Skills | SEO/转化率/文案/增长策略 | 营销 |
| 09 | Skill Creator | 创建自定义 Skill | 开发/自动化 |
