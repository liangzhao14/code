# Git 与 PR 规范

## 分支命名

| 类型 | 格式 | 示例 |
|------|------|------|
| 新功能 | `feature/xxx` | `feature/user-management` |
| Bug 修复 | `fix/xxx` | `fix/login-token-expire` |
| 重构 | `refactor/xxx` | `refactor/order-service` |
| 文档 | `docs/xxx` | `docs/api-design` |
| 热修复 | `hotfix/xxx` | `hotfix/payment-crash` |

## Commit 规范（Conventional Commits）

格式：`type(scope): 简短描述`

| type | 含义 |
|------|------|
| `feat` | 新功能 |
| `fix` | Bug 修复 |
| `refactor` | 重构（不影响功能） |
| `docs` | 文档变更 |
| `test` | 测试相关 |
| `chore` | 构建/依赖/配置变更 |
| `perf` | 性能优化 |

示例：
```
feat(user): 新增用户列表分页查询接口
fix(order): 修复订单金额计算精度问题
refactor(auth): 重构 Token 刷新逻辑
```

## PR 规范

- 单次 PR 变更行数 ≤ 400 行，超出须拆分
- 每个 PR 至少一位同事 Review 通过后合并
- PR 描述须包含：变更背景、影响范围、测试说明
- CI 必须全绿（lint + test + build）才能合并
- 禁止直接向 `main` / `master` 分支推送

## 代码审查要点

- 是否遵循本项目编码规范（命名/异常/日志）
- 是否存在安全隐患（SQL 注入、XSS、敏感信息硬编码）
- 是否有遗漏的错误处理场景
- 单元测试是否覆盖核心逻辑
- 数据库变更是否向后兼容
