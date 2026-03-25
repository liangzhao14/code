# Java 后端编码规范（阿里巴巴 Java 开发手册）

## 命名规范

| 元素 | 规范 | 示例 |
|------|------|------|
| 类名 | UpperCamelCase | `UserService`、`OrderController` |
| 方法/变量 | lowerCamelCase | `getUserById`、`orderList` |
| 常量 | UPPER_SNAKE_CASE | `MAX_RETRY_COUNT` |
| 包名 | 全小写，无下划线 | `com.example.user.service` |
| 枚举类/成员 | UpperCamelCase / UPPER_SNAKE_CASE | `OrderStatus.PENDING` |
| POJO 布尔字段 | 不加 `is` 前缀 | `valid` 非 `isValid` |
| 抽象类 | 以 `Abstract` 开头 | `AbstractBaseService` |
| 异常类 | 以 `Exception` 结尾 | `BusinessException` |
| 测试类 | 以 `Test` 结尾 | `UserServiceTest` |
| DTO/VO | 对应后缀 | `CreateUserDTO`、`UserVO` |

- 接口名不以 `I` 开头；实现类仅必要时加 `Impl` 后缀

## 常量与枚举

- 禁止代码中出现魔法数字或魔法字符串，必须定义命名常量
- 业务常量定义在专用常量类，不用接口定义常量
- 相关常量用带描述字段的枚举分组

```java
public enum OrderStatus {
    PENDING(1, "待支付"), PAID(2, "已支付"), CANCELLED(3, "已取消");
    private final int code;
    private final String desc;
    OrderStatus(int code, String desc) { this.code = code; this.desc = desc; }
}
```

## 方法与类设计

- 单一职责：类和方法只做一件事
- 方法长度 ≤ 80 行，超出提取私有方法
- 方法参数 ≤ 5 个，超出封装为 DTO/请求对象
- 继承层级 ≤ 3 层，优先组合
- `equals()` 和 `hashCode()` 必须同时重写

## 集合规范

- 初始化时指定容量：`new ArrayList<>(16)`
- 判空用 `isEmpty()`，不用 `size() == 0`
- 禁止边迭代边修改集合
- 返回集合类型方法返回 `Collections.emptyList()`，不返回 `null`
- 优先使用 `Map.getOrDefault()` / `computeIfAbsent()`

## Null 安全

- 返回单值可选结果使用 `Optional<T>`
- 方法入口校验参数：`Objects.requireNonNull` 或断言
- 公共 API 边界标注 `@NonNull` / `@Nullable`

## 异常处理

- 捕获具体异常，禁止 `catch (Exception e)` 后吞掉
- 禁止空 catch 块
- 重新抛出前先记录异常及上下文
- 业务规则违反使用自定义 `BusinessException`（非受检）+ 错误码

```java
try {
    orderService.pay(orderId);
} catch (InsufficientBalanceException e) {
    log.warn("支付失败，余额不足: orderId={}", orderId, e);
    throw new BusinessException(ErrorCode.INSUFFICIENT_BALANCE, e);
}
```

## 日志规范（SLF4J）

- 使用占位符格式，禁止字符串拼接：`log.info("id={}", id)`
- `ERROR` 用于系统故障，`WARN` 用于可恢复异常，`INFO` 用于关键业务事件
- 禁止记录密码、Token、身份证号、手机号等敏感信息
- 所有日志包含 traceId 或业务 ID

```java
// 正确
log.info("订单创建成功: orderId={}, userId={}, amount={}", orderId, userId, amount);
// 错误
log.info("订单创建成功: " + orderId);
```

## 事务管理

- `@Transactional` 标注在 Service 方法，不在 DAO 上
- 必须显式指定 `rollbackFor = Exception.class`
- 事务内只做数据库操作，禁止包含远程调用（HTTP/MQ）
- 禁止同类内部自调用 `@Transactional` 方法（绕过代理导致失效）

```java
@Transactional(rollbackFor = Exception.class)
public void createOrder(CreateOrderDTO dto) {
    // 只做 DB 操作；MQ 消息在事务提交后发送
}
```

## 并发规范

- 优先用 `java.util.concurrent` 工具类，少用原生 `synchronized`
- 线程池用 `ThreadPoolExecutor`，显式命名线程和队列容量，禁止 `Executors.newCachedThreadPool()`
- 多线程共享标志位用 `volatile`，计数器用 `AtomicXxx`
- 禁止在共享状态中使用 `SimpleDateFormat`，用线程安全的 `DateTimeFormatter`

## REST 接口设计

- URL：小写 kebab-case，名词资源：`GET /api/v1/orders/{id}`
- HTTP 动词：`GET` 查询、`POST` 创建、`PUT` 全量更新、`PATCH` 部分更新、`DELETE` 删除
- 统一响应体：`{ code, message, data }`（0 表示成功）
- 请求 DTO 使用 Bean Validation（`@NotNull`、`@Size` 等）+ Controller 上 `@Validated`
- 禁止在响应中暴露堆栈信息

## 代码质量门禁

- Service 层单测覆盖率 ≥ 80%
- 所有 public 方法有 Javadoc（用途/参数/返回值/异常）
- 不得提交 Checkstyle / PMD / SpotBugs 告警
- `TODO` / `FIXME` 必须关联工单编号
- 合并前必须通过 Sonar 质量门禁
