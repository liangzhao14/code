#!/bin/bash
# auto-sync.sh — 自动记录变更、更新 README、推送 GitHub
# 由 Claude Code Stop hook 触发

REPO="/c/Users/iflytek/Desktop/code"
cd "$REPO" || exit 0

# 没有变更则退出
if [ -z "$(git status --porcelain)" ]; then
  exit 0
fi

DATE=$(date '+%Y-%m-%d %H:%M')

# ── 1. 生成变更条目 ──────────────────────────────────────────
ENTRY="## $DATE\n\n"
while IFS= read -r line; do
  STATUS="${line:0:2}"
  FILE="${line:3}"
  case "$STATUS" in
    "A "|" A"|"??") ENTRY+="- 新增: $FILE\n" ;;
    "M "|" M")      ENTRY+="- 修改: $FILE\n" ;;
    "D "|" D")      ENTRY+="- 删除: $FILE\n" ;;
    "R "*)          ENTRY+="- 重命名: $FILE\n" ;;
    *)              ENTRY+="- 变更: $FILE\n" ;;
  esac
done < <(git status --porcelain | head -30)

ENTRY+="\n"

# ── 2. 更新 CHANGELOG.md（新记录插入到顶部）───────────────────
TMPFILE=$(mktemp)
# 保留文件头（前5行：标题+说明），将新条目插入其后
HEAD_LINES=$(head -6 CHANGELOG.md)
TAIL_CONTENT=$(tail -n +7 CHANGELOG.md)
{
  echo "$HEAD_LINES"
  echo ""
  echo -e "$ENTRY"
  echo "$TAIL_CONTENT"
} > "$TMPFILE"
mv "$TMPFILE" CHANGELOG.md

# ── 3. 更新 README.md 的「最近变更」区块 ──────────────────────
python - <<'PYEOF'
import re

with open('CHANGELOG.md', 'r', encoding='utf-8') as f:
    changelog = f.read()

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# 取 CHANGELOG 中最新的一条记录（## 日期 ... 下一个 ## 之前）
match = re.search(r'(## \d{4}-\d{2}-\d{2}.*?)(?=\n## |\Z)', changelog, re.DOTALL)
recent = match.group(1).strip() if match else ''

new_section = '## 最近变更\n\n' + recent + '\n'

if '## 最近变更' in readme:
    readme = re.sub(r'## 最近变更.*?(?=\n---|\n## |\Z)', new_section, readme, flags=re.DOTALL)
else:
    readme = readme.rstrip() + '\n\n---\n\n' + new_section + '\n'

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
PYEOF

# ── 4. Git commit & push ───────────────────────────────────────
git add -A

# 生成简洁的提交信息（列出主要变更文件）
SUMMARY=$(git diff --cached --name-only | head -5 | tr '\n' ', ' | sed 's/,$//')
git commit -m "chore: auto-sync ${DATE} — ${SUMMARY}

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"

git push

echo '{"systemMessage": "已自动同步：CHANGELOG 已记录，README 已更新，代码已推送到 GitHub"}'
