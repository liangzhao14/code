# 前端单元测试规范（Vitest）

> 本文件是 `lyspec-unit-test` 的 reference，按需加载。
> 适用于 Vue 3 / React / TypeScript 项目的前端单元测试。

---

## 技术栈

- **测试框架**：Vitest
- **组件测试**：@vue/test-utils（Vue）/ @testing-library/react（React）
- **Mock**：`vi.mock` / `vi.fn` / `vi.spyOn` / `vi.stubGlobal`
- **运行工具**：pnpm / npm

---

## 上游输入

> 若有前端详细设计文档（lyspec-frontend 产物），从以下章节提取测试上下文：

| 详细设计章节 | 提取内容 | 用途 |
|-------------|---------|------|
| 3.1 组件树 | 页面组件拆分和交互行为 | 确定需要测试的组件清单 |
| 3.2 通用组件 | Props / Events 定义 | 推导组件测试的输入输出 |
| 4.2 业务类型定义 | VO / DTO TypeScript 类型 | 构造测试数据 |
| 5.1 Store/Hook 清单 | Store action 和 state | 推导状态管理测试用例 |
| 7.1 HTTP 错误处理 | 各状态码处理方式 | 推导 API 层错误处理测试 |

---

## 运行命令

```bash
# 全部测试
pnpm test

# 监视模式（开发时推荐）
pnpm test:watch

# 带覆盖率
pnpm test:coverage

# 运行指定 workspace 项目
pnpm vitest run --project @xxx/utils

# 运行单个文件
pnpm vitest run src/utils/time.test.ts

# 运行匹配名称的测试
pnpm vitest run -t "formatSecondsToTime"
```

---

## 测试文件规范

### 命名和位置

- 测试文件放在源码**同目录**：`xxx.test.ts`
- 共享测试工具放在 `__tests__/` 目录
- 描述（describe/it）使用**中文**

### 结构模板

```typescript
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { targetFunction } from './target'

describe('targetFunction', () => {
  it('应正确处理正常输入', () => {
    // Arrange
    const input = 'test'
    // Act
    const result = targetFunction(input)
    // Assert
    expect(result).toBe('expected')
  })

  it('边界值应返回默认值', () => {
    expect(targetFunction(null)).toBe('default')
    expect(targetFunction(undefined)).toBe('default')
  })
})
```

---

## 按类型测试策略

### 1. 工具函数测试

> 优先级最高，纯函数测试价值最大。

```typescript
describe('formatDate', () => {
  it('应格式化有效日期', () => {
    expect(formatDate(new Date('2025-01-01'))).toBe('2025-01-01')
  })

  it('应处理无效输入', () => {
    expect(formatDate(null)).toBe('')
    expect(formatDate(undefined)).toBe('')
  })

  it('应处理边界日期', () => {
    expect(formatDate(new Date('1970-01-01'))).toBe('1970-01-01')
  })
})
```

### 2. Composable / Hook 测试

```typescript
import { ref } from 'vue'

describe('useCounter', () => {
  it('应正确增加计数', () => {
    const { count, increment } = useCounter()
    expect(count.value).toBe(0)
    increment()
    expect(count.value).toBe(1)
  })

  it('应支持初始值', () => {
    const { count } = useCounter(10)
    expect(count.value).toBe(10)
  })
})
```

### 3. Pinia Store 测试

```typescript
import { setActivePinia, createPinia } from 'pinia'
import { useUserStore } from './user'

describe('useUserStore', () => {
  beforeEach(() => {
    setActivePinia(createPinia())
  })

  it('login 应正确设置用户信息', async () => {
    const store = useUserStore()
    vi.spyOn(authApi, 'login').mockResolvedValue({ token: 'xxx', user: mockUser })

    await store.login({ username: 'admin', password: '123' })

    expect(store.token).toBe('xxx')
    expect(store.userInfo).toEqual(mockUser)
  })

  it('logout 应清除用户信息', () => {
    const store = useUserStore()
    store.$patch({ token: 'xxx', userInfo: mockUser })

    store.logout()

    expect(store.token).toBe('')
    expect(store.userInfo).toBeNull()
  })
})
```

### 4. Vue 组件测试

```typescript
import { mount } from '@vue/test-utils'
import MyComponent from './MyComponent.vue'

describe('MyComponent', () => {
  it('应根据 props 正确渲染', () => {
    const wrapper = mount(MyComponent, { props: { title: '测试标题' } })
    expect(wrapper.text()).toContain('测试标题')
  })

  it('点击按钮应触发事件', async () => {
    const wrapper = mount(MyComponent)
    await wrapper.find('button').trigger('click')
    expect(wrapper.emitted('submit')).toHaveLength(1)
  })

  it('条件渲染应正确控制显隐', () => {
    const wrapper = mount(MyComponent, { props: { visible: false } })
    expect(wrapper.find('.content').exists()).toBe(false)
  })
})
```

> **AI生成规则**：
> - 组件测试关注**行为**（点击、输入、事件触发），不测试 DOM 结构细节
> - 若有 lyspec-frontend 的组件树，按组件树逐个覆盖
> - 标注每个测试对应的交互行为

### 5. API 层测试

```typescript
import { xxxApi } from './xxx'

vi.mock('@/utils/request', () => ({
  default: {
    get: vi.fn(),
    post: vi.fn(),
    put: vi.fn(),
    delete: vi.fn(),
  },
}))

import request from '@/utils/request'

describe('xxxApi', () => {
  it('list 应发送正确的 GET 请求', async () => {
    const mockResponse = { code: 0, data: { records: [], total: 0 } }
    vi.mocked(request.get).mockResolvedValue(mockResponse)

    const result = await xxxApi.list({ page: 1, size: 10 })

    expect(request.get).toHaveBeenCalledWith('/api/v1/xxx', { params: { page: 1, size: 10 } })
    expect(result).toEqual(mockResponse)
  })
})
```

---

## 设计模式测试策略

### 单例类测试

单例类需要在每个测试文件间隔离：

```typescript
describe('MySingleton', () => {
  let MySingleton: typeof import('./MySingleton').MySingleton

  beforeEach(async () => {
    vi.resetModules()
    const mod = await import('./MySingleton')
    MySingleton = mod.MySingleton
  })

  it('globalInstance 应返回同一实例', () => {
    const a = MySingleton.globalInstance()
    const b = MySingleton.globalInstance()
    expect(a).toBe(b)
  })
})
```

配置要求：vitest.config.ts 中设置 `pool: 'forks'`。

### EventEmitter 测试

```typescript
it('on/emit 应正确触发', () => {
  const handler = vi.fn()
  emitter.on('eventName', handler)
  emitter.emit('eventName', payload)
  expect(handler).toHaveBeenCalledWith(payload)
})
```

必测项：on、off、emit、once 选项、immediate 选项、destroy、链式调用。

### 定时器类测试

```typescript
beforeEach(() => vi.useFakeTimers())
afterEach(() => vi.useRealTimers())

it('应在延迟后执行', () => {
  startTimer()
  vi.advanceTimersByTime(1000)
  expect(callback).toHaveBeenCalled()
})
```

注意：避免 `vi.runAllTimers()` 在无终止条件的定时器中使用，会导致无限循环。

---

## Mock 策略速查

| 目标 | 方法 | 说明 |
|------|------|------|
| markRaw | setup.ts 中 `vi.mock('vue')` 透传 | Vue 内部工具 |
| AudioContext | `vi.stubGlobal('AudioContext', MockClass)` | 浏览器 API |
| HTMLAudioElement | `vi.stubGlobal('Audio', MockAudio)` | 浏览器 API |
| WebSocket | `vi.mock('reconnecting-websocket')` | 网络通信 |
| axios / request | `vi.mock('@/utils/request')` | HTTP 客户端 |
| Cookie | `vi.mock('js-cookie')` | 浏览器存储 |
| 定时器 | `vi.useFakeTimers()` | setTimeout/setInterval |
| Tauri API | `vi.stubGlobal('__TAURI__', mockObj)` | 桌面端 API |
| localStorage | `vi.stubGlobal('localStorage', mockStorage)` | 浏览器存储 |
| window.location | `vi.stubGlobal('location', { href: '...' })` | 路由跳转 |

---

## 失败分析流程

1. 读取失败的测试代码和被测源码
2. 区分失败类型：

| 失败类型 | 原因 | 修复方式 |
|---------|------|---------|
| 断言失败 | 测试预期与源码行为不符 | 修正测试预期值或源码 |
| 导入错误 | 路径别名配置问题 | 检查 vitest.config.ts 的 resolve.alias |
| Mock 不完整 | 缺失浏览器 API Mock | 补充 `vi.stubGlobal` 或 setup.ts |
| 超时/无限循环 | fake timers 使用不当 | 用 `advanceTimersByTime` 替代 `runAllTimers` |
| 类型错误 | TypeScript 类型不匹配 | 检查 Mock 返回值类型 |

3. 修复后重新运行验证

---

## 禁止事项

- 禁止测试实现细节（如检查 DOM class 名、内部变量值）
- 禁止测试之间共享可变状态
- 禁止 `it.skip` 跳过测试（如需临时跳过须附注释说明）
- 禁止为通过测试而修改业务代码
- 禁止在测试中直接操作真实 API（所有 HTTP 请求必须 Mock）
