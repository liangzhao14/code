# Java 单元测试规范（JUnit 5 + Mockito）

> 本文件是 `lyspec-unit-test` 的 reference，按需加载。
> 适用于 Java 17 + Spring Boot 项目的 Service 层单元测试。

---

## 技术栈

- **测试框架**：JUnit 5（`@ExtendWith(MockitoExtension.class)`）
- **Mock 框架**：Mockito（`@Mock` / `@Spy` / `@InjectMocks` / `MockedStatic`）
- **断言库**：AssertJ（`assertThat`）
- **构建工具**：Maven（`mvn test`）

---

## 上游输入

> 若有后端详细设计文档（lyspec-backend 产物），从以下章节提取测试上下文：

| 详细设计章节 | 提取内容 | 用途 |
|-------------|---------|------|
| 4.2 分层职责 | Controller/Service/Mapper 各层职责 | 确定各层测试重点和 Mock 边界 |
| 5.2 异常处理体系 | 异常类层次（BusinessException、AuthException 等） | 异常路径测试必须覆盖的异常类型 |
| 5.3 事务设计 | 事务边界和传播行为 | 验证事务方法的原子性 |
| 3.4 接口详细说明 | 参数校验规则（长度、范围、格式） | 推导边界值测试用例 |
| 3.2 错误码设计 | 业务错误码清单 | 验证 Service 抛出正确的异常和错误码 |

---

## Phase 1：读取目标类

读取被测 ServiceImpl 文件，分析：

- 所有 `public` 方法及其逻辑分支
- 注入的依赖（Mapper、其他 Service）
- 调用的静态工具类（如 `UserContext`、`JsonUtil`）
- 抛出的异常类型和条件
- 父类 `ServiceImpl` 中被调用的方法（`count`、`list`、`saveOrUpdate` 等）

同时读取相关的 Entity、DTO、VO 类，了解字段结构。

> **AI生成规则**：
> - 若有详细设计文档，对照异常体系（5.2节）验证代码中的异常抛出是否完整
> - 识别依赖注入关系，确定需要 Mock 的对象清单

---

## Phase 2：确定测试策略

### 核心原则

| 原则 | 说明 |
|------|------|
| 不启动 Spring 容器 | 禁止使用 `@SpringBootTest`，纯 JUnit + Mockito |
| 隔离外部依赖 | 所有 Mapper、外部 Service 均 Mock |
| 覆盖三类场景 | 正常路径 / 边界条件 / 异常路径 |
| 每个 `@Test` 只验证一个行为 | 遵循 AAA 模式（Arrange-Act-Assert） |

### 输出测试策略表

> 此表须在生成代码前暂停，等待用户确认。

| 被测方法 | 正常路径 | 边界条件 | 异常路径 | 备注 |
|---------|---------|---------|---------|------|
| `createXxx(dto)` | 参数合法，成功创建 | 名称空字符串；字段最大长度 | 名称重复抛 DuplicateKeyException | 从3.4节参数校验推导 |
| `getById(id)` | id存在，返回VO | id=0 | id不存在抛 ResourceNotFoundException | 从5.2节异常体系推导 |

### 针对 MyBatis-Plus ServiceImpl 的策略

由于 `ServiceImpl` 的 `saveOrUpdate`、`count`、`list` 等方法内部依赖 MyBatis-Plus 运行时，
需使用 `@Spy @InjectMocks` 组合，对父类方法做 Stub：

```java
@Spy
@InjectMocks
private XxxServiceImpl xxxService;

// Stub 父类方法，绕过 MyBatis-Plus 运行时依赖
doReturn(true).when(xxxService).saveOrUpdate(any());
doReturn(1L).when(xxxService).count(any());
doReturn(List.of(entity)).when(xxxService).list();
doReturn(List.of(entity)).when(xxxService).list(any());
doReturn(true).when(xxxService).removeById(anyLong());

// super.getById() 通过 mock Mapper 实现
given(xxxMapper.selectById(id)).willReturn(entity);
```

### 静态方法 Mock（如 UserContext）

```java
try (MockedStatic<UserContext> mocked = mockStatic(UserContext.class)) {
    SessionUser mockUser = mock(SessionUser.class);
    given(mockUser.getTeamId()).willReturn("team-001");
    mocked.when(UserContext::getUserDangerously).thenReturn(mockUser);

    // 执行被测方法
}
```

---

## Phase 3：生成测试类

### 文件位置

```
src/
├── main/java/com/xxx/service/impl/XxxServiceImpl.java
└── test/java/com/xxx/service/impl/XxxServiceImplTest.java  ← 与被测类同包
```

### 类骨架

```java
@ExtendWith(MockitoExtension.class)
@DisplayName("XxxService 单元测试")
class XxxServiceImplTest {

    @Mock
    private XxxMapper xxxMapper;

    @Spy
    @InjectMocks
    private XxxServiceImpl xxxService;

    // 公共测试数据
    private XxxEntity mockEntity;

    @BeforeEach
    void setUp() {
        mockEntity = new XxxEntity();
        mockEntity.setId(1L);
    }

    @Nested
    @DisplayName("methodName")
    class MethodName {

        @Test
        @DisplayName("正常场景描述")
        void should_xxx_when_yyy() {
            // Arrange
            // Act
            // Assert
        }
    }
}
```

### 测试方法命名

格式：`should_期望行为_when_前置条件`

| 场景 | 示例 |
|------|------|
| 正常返回 | `should_returnVo_when_entityExists` |
| 返回空 | `should_returnNull_when_entityNotFound` |
| 抛出异常 | `should_throwException_when_nameDuplicate` |
| 不执行操作 | `should_notInsert_when_validationFails` |

### 每个方法必须覆盖的场景

1. **正常路径**：输入合法，验证返回值及关键副作用
2. **边界条件**：空列表、null 字段、空字符串、0 值等
3. **异常路径**：重复校验失败、记录不存在、权限不足等

---

## Phase 4：关键断言模式

### 验证返回值

```java
assertThat(result).isNotNull();
assertThat(result.getId()).isEqualTo(1L);
assertThat(result.getWords()).containsExactly("词A", "词B");
assertThat(result).isNull();
assertThat(list).isEmpty();
assertThat(list).hasSize(2);
```

### 验证异常

```java
assertThatThrownBy(() -> xxxService.doSomething(req))
    .isInstanceOf(RuntimeException.class)
    .hasMessageContaining("名称已存在");
```

### 验证方法调用

```java
// 验证调用次数
then(xxxService).should(times(1)).saveOrUpdate(any());
then(xxxService).should(never()).saveOrUpdate(any());

// 捕获参数验证细节
ArgumentCaptor<XxxEntity> captor = ArgumentCaptor.forClass(XxxEntity.class);
then(xxxService).should().saveOrUpdate(captor.capture());
assertThat(captor.getValue().getWordList()).isEqualTo("[]");
```

---

## Phase 5：执行测试

```bash
# 运行单个测试类
mvn test -pl <module-name> -Dtest=XxxServiceImplTest

# 运行全部测试
mvn test -pl <module-name>

# 带覆盖率报告（Jacoco）
mvn test -pl <module-name> jacoco:report
```

---

## Phase 6：分析失败并修复

对每条失败用例：

1. 读取失败的堆栈信息，定位根本原因：

| 异常类型 | 原因 | 修复方式 |
|---------|------|---------|
| `NullPointerException` | 缺少 Mock 或 Stub | 补充 `given().willReturn()` |
| `WantedButNotInvoked` | 断言方法未被调用 | 检查业务逻辑分支条件 |
| `UnfinishedStubbingException` | `when().thenReturn()` 未完整 | 补全 Stub 链 |
| `UnnecessaryStubbingException` | 多余的 Stub | 删除无效 Stub 或使用 `lenient()` |
| `MissingMethodInvocationException` | `doReturn().when()` 对象非 Mock/Spy | 检查注解配置 |

2. 修复测试代码，**不修改业务代码**
3. 重新执行验证

---

## Phase 7：输出报告

```markdown
### 测试执行报告

**测试类**：XxxServiceImplTest
**测试文件**：src/test/java/com/xxx/service/impl/XxxServiceImplTest.java

**覆盖方法**：
| 方法 | 正常路径 | 边界条件 | 异常路径 |
|------|---------|---------|---------|
| createOrUpdate | ✅ | ✅ | ✅ |
| getById        | ✅ | ✅ | ✅ |
| delete         | ✅ | -  | -  |
| listXxx        | ✅ | ✅ | -  |

**执行结果**：
- 总用例数：N
- 通过：N
- 失败：N
- 跳过：N

**编译 & 运行状态**：✅ 通过 / ❌ 失败（附失败原因）
```

---

## 禁止事项

- 禁止使用 `@SpringBootTest`（不加载 Spring 容器）
- 禁止 Mock 被测类自身（`@Spy` 的部分 Stub 除外）
- 禁止测试之间共享可变状态（每个 `@Test` 独立）
- 禁止为通过测试而修改业务代码
- 禁止仅测试 getter/setter，关注业务行为
