# lingyang Upload 上传

**类型**: JSX 组件（受控/非受控均支持）

---

## 子组件

| 组件 | 说明 |
|------|------|
| `<Upload>` | 主上传组件，点击触发或配合 `drag` prop 开启拖拽 |
| `<Upload.Dragger>` | 语义化拖拽上传区域，等价于 `<Upload drag>` |

---

## 快速参考

| 场景 | 使用方式 |
|------|---------|
| 基本点击上传 | `<Upload action="/api/upload"><Button>选择文件</Button></Upload>` |
| 拖拽上传 | `<Upload drag action="/api/upload">` 或 `<Upload.Dragger action="/...">` |
| 多文件 | `<Upload multiple action="/api/upload">` |
| 文件夹上传 | `<Upload directory action="/api/upload">` |
| 限制类型 | `<Upload accept="image/*,.pdf">` |
| 限制数量 | `<Upload limit={3}>` |
| 图片卡片模式 | `<Upload listType="picture-card" action="/api/upload">` |
| 手动上传 | `<Upload autoUpload={false} onChange={handleChange}>` |
| 自定义请求 | `<Upload customRequest={myRequest}>` |
| 受控文件列表 | `<Upload fileList={list} onChange={(list) => setList(list)}>` |
| 重新上传回调 | `<Upload onReupload={(file) => reupload(file)}>` |
| 超限回调 | `<Upload limit={3} onExceedLimit={(files) => alert('超出数量')}>` |

---

## 与 Ant Design 的 9 个关键差异（易错点）

> ⚠️ 以下差异导致 Ant Design 代码迁移时最容易出 Bug：

1. **onChange 参数结构不同**
   - lingyang: `onChange={(fileList, file) => ...}`，第一参数直接是**完整 fileList 数组**
   - Ant Design: `onChange={({ fileList, file, event }) => ...}`，参数是**解构对象**

2. **文件对象中原始 File 的字段名不同**
   - lingyang: `file.originFile`（File 对象）
   - Ant Design: `file.originFileObj`（File 对象）

3. **listType 枚举不同**
   - lingyang: 有 `'picture-list'`（横向卡片列表，lingyang 专有）
   - Ant Design: 有 `'picture-circle'`（圆形预览，Ant Design 专有）

4. **autoUpload（lingyang 专有）**
   - lingyang: `autoUpload={false}` 直接控制选文件后不立即上传
   - Ant Design: 需在 `beforeUpload` 返回 `false` 配合手动触发实现

5. **customRequest 返回值不同**
   - lingyang: `customRequest` 需返回 `{ abort?: () => void }` 对象
   - Ant Design: `customRequest` 无返回值

6. **onReupload（lingyang 专有）**
   - lingyang: `onReupload={(file) => ...}` 失败文件点击重试时触发
   - Ant Design: 无此回调，需通过 `itemRender` 自定义实现

7. **文件状态多了 'init'**
   - lingyang: `status: 'init' | 'uploading' | 'done' | 'error'`（`init` = 已选择待上传）
   - Ant Design: `status: 'uploading' | 'done' | 'error' | 'removed'`（无 `init`，多 `removed`）

8. **自定义文件列表的 API 名不同**
   - lingyang: `renderUploadItem` / `renderUploadList`
   - Ant Design: `itemRender` / `（无直接对应，需通过 showUploadList=false 自定义）`

9. **beforeUpload 返回值不同**
   - lingyang: 返回 `false` 或 `Promise.reject` 阻止；返回新 `File` 可替换文件
   - Ant Design: 额外支持返回 `Upload.LIST_IGNORE`（选择文件后不加入列表）

---

## Props 速查表

| Prop | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| fileList | `UploadItem[]` | — | 受控：文件列表 |
| defaultFileList | `UploadItem[]` | `[]` | 非受控：初始文件列表 |
| action | `string \| (file) => Promise<string>` | — | 上传目标 URL |
| method | string | `'post'` | 请求方法 |
| headers | `object \| (file) => object` | — | 请求头 |
| data | `object \| (file) => object` | — | 附加参数 |
| name | `string \| (file) => string` | `'file'` | FormData 字段名 |
| withCredentials | boolean | `false` | 是否携带 Cookie |
| accept | string | — | 允许的文件类型 |
| multiple | boolean | `false` | 是否多文件选择 |
| directory | boolean | `false` | 是否文件夹上传 |
| drag | boolean | `false` | 是否开启拖拽模式 |
| disabled | boolean | `false` | 是否禁用 |
| limit | `number \| { maxCount, hideOnExceedLimit? }` | — | 最大上传数量 |
| autoUpload | boolean | `true` | 是否自动上传（**lingyang 专有**） |
| listType | `'text'\|'picture'\|'picture-card'\|'picture-list'` | `'text'` | 列表展示类型（含 picture-list） |
| showUploadList | `boolean \| object` | `true` | 是否显示文件列表（对象可自定义图标） |
| renderUploadItem | `(node, file, list) => ReactNode` | — | 自定义单个文件项渲染（**不是 itemRender**） |
| renderUploadList | `(list, props) => ReactNode` | — | 完全自定义文件列表渲染 |
| beforeUpload | `(file, fileList) => boolean \| Promise` | — | 上传前钩子 |
| customRequest | `(options: RequestOptions) => { abort? }` | — | 自定义上传请求（需返回对象） |
| onChange | `(fileList: UploadItem[], file: UploadItem) => void` | — | 文件列表变化（**第一参数是数组**） |
| onProgress | `(file, e) => void` | — | 上传进度回调 |
| onSuccess | `(file) => void` | — | 上传成功回调 |
| onError | `(file, response?) => void` | — | 上传失败回调 |
| onRemove | `(file, list) => void \| boolean \| Promise` | — | 移除文件回调（返回 false 阻止） |
| onPreview | `(file) => void` | — | 点击预览回调 |
| onReupload | `(file) => void` | — | 重新上传回调（**lingyang 专有**） |
| onExceedLimit | `(files, list) => void` | — | 超出数量限制回调 |
| imagePreview | boolean | `false` | picture-card 模式下使用内置图片预览 |
| tip | `string \| ReactNode` | — | 触发器下方的提示文字 |

### UploadItem 文件数据结构

```typescript
interface UploadItem {
  uid: string;                                      // 唯一标识
  name?: string;                                    // 文件名
  url?: string;                                     // 文件/预览 URL
  status?: 'init' | 'uploading' | 'done' | 'error'; // 状态（含 init，Ant Design 无）
  percent?: number;                                 // 上传进度 0-100
  originFile?: File;                                // 原始 File（注意：不是 originFileObj）
  response?: any;                                   // 响应数据
  thumbUrl?: string;                                // 缩略图 URL
}
```

### RequestOptions（customRequest 参数）

```typescript
interface RequestOptions {
  file: File;
  action: string;
  headers: object;
  data: object;
  name: string;
  withCredentials: boolean;
  onProgress: (percent: number, event?: ProgressEvent) => void;
  onSuccess: (response?: any) => void;
  onError: (response?: any) => void;
}
```

---

## 常用 CSS 类名

`.lingyang-upload` / `.lingyang-upload-trigger` / `.lingyang-upload-trigger-disabled` / `.lingyang-upload-drag` / `.lingyang-upload-drag-active` / `.lingyang-upload-list` / `.lingyang-upload-list-item` / `.lingyang-upload-list-item-{done|error|uploading}` / `.lingyang-upload-list-picture-card` / `.lingyang-upload-list-picture-list` / `.lingyang-upload-list-item-progress` / `.lingyang-upload-tip`

---

## 参考文件

- 完整代码示例（8 个场景）→ `references/examples.md`
- 完整 TypeScript 接口定义 + 差异对比表 → `references/props.md`
-e 

---

## 完整代码示例

# lingyang Upload — 完整代码示例

## 1. 基本点击上传

```jsx
import { Upload, Button } from 'lingyang';
import { IconUpload } from 'lingyang/icon';

function BasicUpload() {
  return (
    <Upload
      action="/api/upload"
      // onChange 第一参数直接是 fileList 数组
      // 注意：Ant Design 是 ({ fileList, file }) => {}
      onChange={(fileList, file) => {
        console.log('文件列表：', fileList);
        console.log('当前变化文件：', file);
        console.log('原始 File 对象：', file.originFile); // 注意：不是 originFileObj
      }}
      onSuccess={(file) => console.log('上传成功：', file.response)}
      onError={(file) => console.log('上传失败：', file.response)}
    >
      <Button icon={<IconUpload />}>点击上传</Button>
    </Upload>
  );
}
```

---

## 2. 受控文件列表

```jsx
import { useState } from 'react';
import { Upload, Button } from 'lingyang';
import { IconUpload } from 'lingyang/icon';

function ControlledUpload() {
  const [fileList, setFileList] = useState([
    // 已有文件（如服务端返回的初始数据）
    {
      uid: 'exist-1',
      name: 'avatar.png',
      url: 'https://example.com/avatar.png',
      status: 'done',
    },
  ]);

  return (
    <Upload
      fileList={fileList}
      action="/api/upload"
      // 受控模式：onChange 回调中更新 fileList
      onChange={(list) => setFileList(list)}
      onRemove={(file) => {
        // 返回 false 可阻止删除
        console.log('删除文件：', file.uid);
      }}
    >
      <Button icon={<IconUpload />}>上传文件</Button>
    </Upload>
  );
}
```

---

## 3. 拖拽上传（Upload.Dragger）

```jsx
import { Upload } from 'lingyang';
import { IconUpload } from 'lingyang/icon';

function DragUpload() {
  return (
    // Upload.Dragger 等价于 <Upload drag>，语义化写法
    <Upload.Dragger
      action="/api/upload"
      multiple
      accept="image/*,.pdf"
      onChange={(fileList, file) => console.log(fileList)}
      tip="支持 JPG、PNG、PDF，单文件不超过 10MB"
    >
      <div style={{ textAlign: 'center', padding: '40px 0' }}>
        <IconUpload style={{ fontSize: 48, color: '#165DFF' }} />
        <p style={{ marginTop: 12, color: '#4E5969' }}>点击或拖拽文件到此区域上传</p>
        <p style={{ color: '#86909C', fontSize: 12 }}>支持 JPG、PNG、PDF，单文件不超过 10MB</p>
      </div>
    </Upload.Dragger>
  );
}
```

---

## 4. 图片卡片模式（listType="picture-card"）

```jsx
import { useState } from 'react';
import { Upload } from 'lingyang';
import { IconPlus } from 'lingyang/icon';

function PictureCardUpload() {
  const [fileList, setFileList] = useState([]);

  // beforeUpload：校验文件大小和类型
  const beforeUpload = (file) => {
    const isImage = file.type.startsWith('image/');
    if (!isImage) {
      // 返回 false 阻止上传
      console.error('只能上传图片文件');
      return false;
    }
    const isLt2M = file.size / 1024 / 1024 < 2;
    if (!isLt2M) {
      console.error('图片大小不能超过 2MB');
      return false;
    }
    return true;
  };

  return (
    <Upload
      listType="picture-card"
      fileList={fileList}
      action="/api/upload"
      accept="image/*"
      multiple
      limit={8}
      beforeUpload={beforeUpload}
      onChange={(list) => setFileList(list)}
      // imagePreview：点击图片时使用内置 Preview 组件预览
      imagePreview
      onPreview={(file) => console.log('预览：', file.url)}
    >
      {/* 触发区域：达到 limit 后自动隐藏 */}
      <div style={{ textAlign: 'center' }}>
        <IconPlus style={{ fontSize: 24, color: '#86909C' }} />
        <p style={{ marginTop: 4, color: '#86909C', fontSize: 12 }}>上传图片</p>
      </div>
    </Upload>
  );
}
```

---

## 5. 手动上传（autoUpload=false — lingyang 专有）

```jsx
import { useState, useRef } from 'react';
import { Upload, Button, Space } from 'lingyang';
import { IconUpload, IconSend } from 'lingyang/icon';

function ManualUpload() {
  const [fileList, setFileList] = useState([]);

  const handleSubmit = () => {
    // 手动触发所有 status='init' 的文件上传
    // 实际场景中可调用自定义请求逻辑或配合 form 提交
    const pendingFiles = fileList.filter(f => f.status === 'init');
    console.log('待上传文件：', pendingFiles.map(f => f.originFile));
    // 可在这里调用 form.submit() 或手动 fetch
  };

  return (
    <div>
      {/*
        autoUpload={false}：选择文件后不立即上传，状态为 'init'
        【lingyang 专有】Ant Design 需通过 beforeUpload 返回 false 实现
      */}
      <Upload
        autoUpload={false}
        fileList={fileList}
        onChange={(list) => setFileList(list)}
        multiple
        accept=".jpg,.png,.pdf"
      >
        <Button icon={<IconUpload />}>选择文件</Button>
      </Upload>

      <Space style={{ marginTop: 16 }}>
        <Button
          type="primary"
          icon={<IconSend />}
          disabled={!fileList.some(f => f.status === 'init')}
          onClick={handleSubmit}
        >
          开始上传（{fileList.filter(f => f.status === 'init').length} 个文件）
        </Button>
        <Button onClick={() => setFileList([])}>清空</Button>
      </Space>
    </div>
  );
}
```

---

## 6. 自定义上传请求（customRequest）

```jsx
import { Upload, Button } from 'lingyang';
import { IconUpload } from 'lingyang/icon';

function CustomRequestUpload() {
  /**
   * 自定义上传请求。
   * 注意：lingyang customRequest 需返回 { abort?: () => void }
   * Ant Design 的 customRequest 无返回值
   */
  const customRequest = (options) => {
    const { file, action, headers, data, onProgress, onSuccess, onError } = options;

    const formData = new FormData();
    formData.append('file', file);
    if (data) {
      Object.keys(data).forEach(key => formData.append(key, data[key]));
    }

    const xhr = new XMLHttpRequest();

    xhr.upload.onprogress = (e) => {
      if (e.total > 0) {
        const percent = Math.round((e.loaded / e.total) * 100);
        onProgress(percent, e);
      }
    };

    xhr.onload = () => {
      if (xhr.status >= 200 && xhr.status < 300) {
        try {
          const response = JSON.parse(xhr.responseText);
          onSuccess(response);
        } catch {
          onSuccess(xhr.responseText);
        }
      } else {
        onError({ status: xhr.status, message: '上传失败' });
      }
    };

    xhr.onerror = () => onError({ message: '网络错误' });

    xhr.open('POST', action, true);
    if (headers) {
      Object.keys(headers).forEach(key => xhr.setRequestHeader(key, headers[key]));
    }
    xhr.send(formData);

    // 返回 abort 方法供取消上传使用（lingyang 专有要求）
    return { abort: () => xhr.abort() };
  };

  return (
    <Upload
      action="/api/upload"
      customRequest={customRequest}
      onChange={(fileList) => console.log(fileList)}
    >
      <Button icon={<IconUpload />}>自定义上传</Button>
    </Upload>
  );
}
```

---

## 7. 限制数量 + 超限回调 + 重新上传

```jsx
import { useState } from 'react';
import { Upload, Button, Message } from 'lingyang';
import { IconUpload } from 'lingyang/icon';

function LimitUpload() {
  const [fileList, setFileList] = useState([]);

  return (
    <Upload
      action="/api/upload"
      fileList={fileList}
      onChange={(list) => setFileList(list)}
      // 最多 3 个文件，超出后隐藏触发器
      limit={3}
      onExceedLimit={(files) => {
        Message.warning(`最多上传 3 个文件，已忽略 ${files.length} 个`);
      }}
      // onReupload：点击失败文件的重新上传按钮时触发（lingyang 专有）
      // Ant Design 无此回调，需通过 itemRender 自定义实现
      onReupload={(file) => {
        console.log('重新上传：', file.name);
        // 在此手动触发重新上传逻辑
      }}
    >
      <Button icon={<IconUpload />}>上传（最多 3 个）</Button>
    </Upload>
  );
}
```

---

## 8. 自定义文件列表渲染（renderUploadItem）

```jsx
import { useState } from 'react';
import { Upload, Button, Progress, Space } from 'lingyang';
import { IconUpload, IconFile, IconDelete, IconRefresh } from 'lingyang/icon';

function CustomListUpload() {
  const [fileList, setFileList] = useState([]);

  return (
    <Upload
      action="/api/upload"
      fileList={fileList}
      onChange={(list) => setFileList(list)}
      showUploadList={false}
      // renderUploadItem：自定义单个文件项的渲染
      // 注意：lingyang 用 renderUploadItem，Ant Design 用 itemRender
      renderUploadItem={(originNode, file) => (
        <div
          key={file.uid}
          style={{
            display: 'flex',
            alignItems: 'center',
            padding: '8px 12px',
            border: '1px solid #E5E6EB',
            borderRadius: 4,
            marginTop: 8,
            gap: 8,
          }}
        >
          <IconFile style={{ color: '#165DFF', flexShrink: 0 }} />
          <span style={{ flex: 1, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
            {file.name}
          </span>
          {file.status === 'uploading' && (
            <Progress percent={file.percent} style={{ width: 100 }} size="small" />
          )}
          {file.status === 'error' && (
            <span style={{ color: '#F53F3F', fontSize: 12 }}>上传失败</span>
          )}
          {file.status === 'done' && (
            <span style={{ color: '#00B42A', fontSize: 12 }}>已上传</span>
          )}
          <Button
            type="text"
            size="mini"
            icon={<IconDelete />}
            status="danger"
            onClick={() => setFileList(fileList.filter(f => f.uid !== file.uid))}
          />
        </div>
      )}
    >
      <Button icon={<IconUpload />}>选择文件</Button>
    </Upload>
  );
}
```

---

## 9. 在 Form 中使用上传组件

```jsx
import { useState } from 'react';
import { Form, Upload, Button } from 'lingyang';
import { IconUpload } from 'lingyang/icon';

function FormWithUpload() {
  const [form] = Form.useForm();

  const handleSubmit = (values) => {
    console.log('提交：', values);
    // values.avatar 是 UploadItem 数组
  };

  return (
    <Form form={form} layout="vertical" onSubmit={handleSubmit} style={{ width: 400 }}>
      <Form.Item
        field="documents"
        label="上传文件"
        rules={[{
          validator: (value, cb) => {
            if (!value || value.length === 0) return cb('请上传至少一个文件');
            if (value.some(f => f.status === 'error')) return cb('存在上传失败的文件');
            cb();
          }
        }]}
        // triggerPropName + trigger 配置让 Form.Item 正确收集 Upload 的值
        triggerPropName="fileList"
        trigger="onChange"
      >
        <Upload
          action="/api/upload"
          multiple
          limit={5}
          listType="picture"
        >
          <Button icon={<IconUpload />}>点击上传</Button>
        </Upload>
      </Form.Item>

      <Button type="primary" htmlType="submit">提交</Button>
    </Form>
  );
}
```
-e 

---

## 完整 TypeScript 类型定义

# lingyang Upload — 完整 TypeScript 接口定义

## UploadProps

```typescript
interface UploadProps {
  /** 受控：文件列表 */
  fileList?: UploadItem[];
  /** 非受控：初始文件列表。默认 [] */
  defaultFileList?: UploadItem[];
  /**
   * 上传的目标 URL。
   * 支持字符串或返回 Promise<string> 的函数（动态 URL 场景）
   */
  action?: string | ((file: File) => Promise<string>);
  /** 上传请求的 HTTP 方法。默认 'post' */
  method?: string;
  /**
   * 上传请求头。
   * 支持对象或返回对象的函数
   */
  headers?: object | ((file: File) => object);
  /**
   * 上传请求携带的额外参数（附加到 FormData）。
   * 支持对象或返回对象的函数
   */
  data?: object | ((file: File) => object);
  /**
   * 上传文件的 FormData 字段名。默认 'file'。
   * 支持字符串或返回字符串的函数
   */
  name?: string | ((file: File) => string);
  /** 是否携带 Cookie（跨域时配合 CORS 使用）。默认 false */
  withCredentials?: boolean;
  /**
   * 允许上传的文件类型。
   * 支持 MIME 类型（如 'image/*'）或扩展名（如 '.jpg,.png'）
   */
  accept?: string;
  /** 是否允许同时选择多个文件。默认 false */
  multiple?: boolean;
  /** 是否允许上传整个文件夹（需浏览器支持）。默认 false */
  directory?: boolean;
  /** 是否开启拖拽上传模式。默认 false（等价于使用 Upload.Dragger） */
  drag?: boolean;
  /** 是否禁用上传。默认 false */
  disabled?: boolean;
  /**
   * 最大上传文件数量。
   * 传数字：超出后隐藏上传触发器
   * 传对象：{ maxCount: number; hideOnExceedLimit?: boolean } 可控制是否隐藏
   */
  limit?: number | { maxCount: number; hideOnExceedLimit?: boolean };
  /**
   * 【lingyang 专有】选择文件后是否自动开始上传。默认 true。
   * false 时：文件加入列表但状态为 'init'，需手动调用 submit() 或自定义触发
   * Ant Design 无此属性，需通过 beforeUpload 返回 false + 手动触发实现
   */
  autoUpload?: boolean;
  /**
   * 文件列表展示类型。默认 'text'。
   * 【差异】lingyang 有 'picture-list'（横向卡片列表），Ant Design 有 'picture-circle'（圆形预览）
   */
  listType?: 'text' | 'picture' | 'picture-card' | 'picture-list';
  /**
   * 是否展示文件列表。默认 true。
   * 传对象可自定义各操作图标：
   * {
   *   previewIcon?: ReactNode | ((file) => ReactNode)
   *   removeIcon?: ReactNode | ((file) => ReactNode)
   *   fileIcon?: ReactNode | ((file) => ReactNode)
   *   reuploadIcon?: ReactNode | ((file) => ReactNode)
   *   cancelIcon?: ReactNode | ((file) => ReactNode)
   *   startIcon?: ReactNode | ((file) => ReactNode)
   *   errorIcon?: ReactNode | ((file) => ReactNode)
   *   fileName?: (file: UploadItem) => ReactNode
   *   extra?: (file: UploadItem) => ReactNode
   * }
   */
  showUploadList?: boolean | ShowUploadListConfig;
  /**
   * 完全自定义文件列表的渲染函数（替换整个列表区域）。
   * 【差异】lingyang 用 renderUploadList，Ant Design 无直接对应（需 showUploadList=false 自定义）
   */
  renderUploadList?: (fileList: UploadItem[], uploadListProps: object) => ReactNode;
  /**
   * 自定义单个文件列表项的渲染函数。
   * 【差异】lingyang 用 renderUploadItem，Ant Design 用 itemRender
   */
  renderUploadItem?: (originNode: ReactNode, file: UploadItem, fileList: UploadItem[]) => ReactNode;
  /**
   * 上传前的钩子函数。
   * - 返回 false 或 Promise.reject：阻止此文件上传
   * - 返回新 File 对象：替换原文件后上传
   * 【差异】Ant Design 额外支持返回 Upload.LIST_IGNORE（不加入文件列表）；lingyang 无此值
   */
  beforeUpload?: (file: File, fileList: File[]) => boolean | Promise<File | boolean>;
  /**
   * 自定义上传请求函数，完全接管上传逻辑。
   * 【差异】lingyang 需返回 { abort?: () => void } 对象（用于取消上传）；
   * Ant Design 的 customRequest 无返回值
   */
  customRequest?: (options: RequestOptions) => { abort?: () => void };
  /**
   * 文件列表变化回调。
   * 【差异】lingyang 第一参数为完整 UploadItem[]；
   * Ant Design 参数为解构对象 { fileList, file, event }
   */
  onChange?: (fileList: UploadItem[], file: UploadItem) => void;
  /** 上传进度更新回调 */
  onProgress?: (file: UploadItem, e: ProgressEvent) => void;
  /** 文件上传成功回调 */
  onSuccess?: (file: UploadItem) => void;
  /** 文件上传失败回调 */
  onError?: (file: UploadItem, response?: any) => void;
  /**
   * 文件被移除前的回调。
   * 返回 false 或 Promise.resolve(false) 可阻止移除
   */
  onRemove?: (file: UploadItem, fileList: UploadItem[]) => void | boolean | Promise<boolean>;
  /** 点击文件预览时的回调 */
  onPreview?: (file: UploadItem) => void;
  /**
   * 【lingyang 专有】点击重新上传（失败文件的重试按钮）时的回调。
   * Ant Design 无此回调，需通过 itemRender 自定义按钮实现
   */
  onReupload?: (file: UploadItem) => void;
  /** 超出 limit 数量时的回调 */
  onExceedLimit?: (files: File[], fileList: UploadItem[]) => void;
  /**
   * 是否在 picture-card 模式下点击时使用内置 Preview 组件展示图片。
   * 默认 false
   */
  imagePreview?: boolean;
  /** 传递给进度条组件的额外属性 */
  progressProps?: object;
  /** 上传触发器区域（点击此区域触发文件选择） */
  children?: ReactNode;
  /** 提示文字，展示在触发器下方 */
  tip?: string | ReactNode;
  className?: string;
  style?: CSSProperties;
}
```

## UploadItem（文件对象数据结构）

```typescript
interface UploadItem {
  /** 文件唯一标识（自动生成或手动指定） */
  uid: string;
  /** 文件名 */
  name?: string;
  /** 文件 URL（已上传文件或预览地址） */
  url?: string;
  /**
   * 文件状态。
   * 【差异】lingyang 有 'init'（已选择待上传），Ant Design 无 'init' 但有 'removed'
   * 'init'      = 已选择但未上传（autoUpload=false 时）
   * 'uploading' = 上传中
   * 'done'      = 上传成功
   * 'error'     = 上传失败
   */
  status?: 'init' | 'uploading' | 'done' | 'error';
  /** 上传进度（0-100） */
  percent?: number;
  /**
   * 原始 File 对象。
   * 【差异】lingyang 字段名为 originFile；Ant Design 为 originFileObj
   */
  originFile?: File;
  /** 上传请求的响应数据（成功或失败均有） */
  response?: any;
  /** 缩略图 URL（图片文件自动生成） */
  thumbUrl?: string;
}
```

## RequestOptions（customRequest 函数的参数）

```typescript
interface RequestOptions {
  /** 原始 File 对象 */
  file: File;
  /** 上传目标 URL */
  action: string;
  /** 请求头 */
  headers: object;
  /** 附加参数 */
  data: object;
  /** FormData 字段名 */
  name: string;
  /** 是否携带 Cookie */
  withCredentials: boolean;
  /** 更新进度的回调（percent: 0-100） */
  onProgress: (percent: number, event?: ProgressEvent) => void;
  /** 上传成功的回调 */
  onSuccess: (response?: any) => void;
  /** 上传失败的回调 */
  onError: (response?: any) => void;
}
```

## 与 Ant Design 完整差异对比表

| 特性 | lingyang | Ant Design |
|------|---------|------------|
| onChange 参数 | `(fileList: UploadItem[], file: UploadItem)` | `({ fileList, file, event })` 解构对象 |
| 原始文件字段名 | `file.originFile` | `file.originFileObj` |
| 文件状态枚举 | `'init' \| 'uploading' \| 'done' \| 'error'` | `'uploading' \| 'done' \| 'error' \| 'removed'` |
| listType | `'text' \| 'picture' \| 'picture-card' \| 'picture-list'` | `'text' \| 'picture' \| 'picture-card' \| 'picture-circle'` |
| 自动上传 | `autoUpload={false}` 直接控制 | ❌ 需 `beforeUpload` 返回 `false` 实现 |
| customRequest 返回值 | 需返回 `{ abort?: () => void }` | 无返回值 |
| 重新上传回调 | `onReupload` ✅ | ❌ 需 itemRender 自定义 |
| 自定义文件项渲染 | `renderUploadItem` | `itemRender` |
| 自定义整个列表 | `renderUploadList` | ❌ 需 `showUploadList=false` 自定义 |
| beforeUpload 额外返回值 | 无 LIST_IGNORE | 支持 `Upload.LIST_IGNORE` |

---
