# 数据库规范：KingbaseES（PGSQL 模式）

KingbaseES 使用 PGSQL 兼容语法，遵循 PostgreSQL 语法规范，禁止使用 KingbaseES 私有语法以确保可迁移性。

## 建表规范

每张表必须包含以下标准字段：

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | `BIGSERIAL` 或 `BIGINT` | 主键（自增或雪花 ID） |
| `created_at` | `TIMESTAMPTZ` | 创建时间，默认 `NOW()` |
| `updated_at` | `TIMESTAMPTZ` | 更新时间，默认 `NOW()` |
| `deleted` | `BOOLEAN` | 软删除标志，默认 `FALSE` |

- 表名、字段名：全小写，下划线分隔（`snake_case`），业务前缀统一（如 `t_`）
- 字符串字段用 `VARCHAR(n)`，不用 `TEXT` 除非确实无长度限制
- 时间字段统一用 `TIMESTAMPTZ`（含时区），不用 `TIMESTAMP`
- 每张表和每个字段必须添加 `COMMENT`
- 禁止使用 `CHAR` 定长字段

## DDL 示例

```sql
CREATE TABLE t_user (
    id          BIGSERIAL    PRIMARY KEY,
    name        VARCHAR(64)  NOT NULL,
    phone       VARCHAR(20)  NOT NULL,
    dept_id     BIGINT       NOT NULL,
    status      SMALLINT     NOT NULL DEFAULT 1,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    deleted     BOOLEAN      NOT NULL DEFAULT FALSE
);

COMMENT ON TABLE  t_user          IS '用户表';
COMMENT ON COLUMN t_user.id       IS '主键';
COMMENT ON COLUMN t_user.name     IS '用户姓名';
COMMENT ON COLUMN t_user.phone    IS '手机号（AES加密存储）';
COMMENT ON COLUMN t_user.dept_id  IS '所属部门ID';
COMMENT ON COLUMN t_user.status   IS '状态：1正常 0禁用';
COMMENT ON COLUMN t_user.deleted  IS '软删除标志';

CREATE INDEX idx_t_user_dept_id ON t_user (dept_id) WHERE deleted = FALSE;
CREATE INDEX idx_t_user_phone   ON t_user (phone)   WHERE deleted = FALSE;
```

## 索引规范

- 外键列必须建索引
- 高选择性查询列（如手机号、邮箱、编号）建普通索引
- 复合索引遵循最左前缀原则，将高区分度字段放左侧
- 频繁查询的过滤条件（如 `deleted = FALSE`）使用**局部索引（Partial Index）**
- 单表索引数量一般不超过 5 个，避免影响写性能
- 禁止对大文本字段（`TEXT` / `VARCHAR(1000+)`）直接建 B-tree 索引

## SQL 编写规范

- **禁止 `SELECT *`**，始终显式列出查询字段
- **禁止拼接用户输入构造 SQL**，使用 MyBatis `#{}` 参数绑定（禁止 `${}`）
- 批量操作使用 MyBatis `<foreach>` 或 JDBC `executeBatch`，禁止在 Java 中循环单条 SQL
- 分页查询必须带 `LIMIT` 和 `OFFSET`，禁止一次性查全表
- 软删除场景所有查询必须加 `WHERE deleted = FALSE`

```sql
-- 分页查询示例
SELECT id, name, phone, status
FROM t_user
WHERE deleted = FALSE
  AND dept_id = #{deptId}
  AND (#{keyword} IS NULL OR name LIKE CONCAT('%', #{keyword}, '%'))
ORDER BY created_at DESC
LIMIT #{size} OFFSET #{offset};
```

## 锁与并发

- 库存/余额等高竞争场景使用悲观锁：`SELECT ... FOR UPDATE`
- 低竞争更新使用乐观锁：表中增加 `version BIGINT NOT NULL DEFAULT 0` 字段

```sql
-- 乐观锁更新
UPDATE t_user
SET name = #{name}, version = version + 1, updated_at = NOW()
WHERE id = #{id} AND version = #{version} AND deleted = FALSE;
```

## KingbaseES 特性速查

| 特性 | 说明 |
|------|------|
| 兼容模式 | PGSQL 模式，支持 PostgreSQL 语法和扩展 |
| 自增主键 | 使用 `BIGSERIAL` 或 `CREATE SEQUENCE` |
| JSON 支持 | 支持 `JSONB` 类型及 `->`、`->>`、`@>` 操作符 |
| 全文检索 | 支持 `tsvector` / `tsquery`（与 PG 兼容） |
| 常用函数 | `NOW()`、`COALESCE()`、`STRING_AGG()`、`ARRAY_AGG()` 等 |
| 窗口函数 | `ROW_NUMBER()`、`RANK()`、`LAG()`、`LEAD()` 等 |
| 禁用特性 | 不使用 KingbaseES 私有语法，确保可迁移性 |
