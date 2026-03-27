import { appRows, resultRows } from "../data/mockData";

const wait = (ms = 120) => new Promise((resolve) => setTimeout(resolve, ms));

const appDetail = {
  id: "APP_91KD28A",
  name: "CaseGen-ERP",
  status: "启用中",
  baseInfo: [
    { label: "应用名称", value: "CaseGen-ERP" },
    { label: "应用标识", value: "APP_91KD28A" },
    { label: "创建时间", value: "2026-03-22 10:40" },
    { label: "联系人", value: "刘洋 / liuyang@example.com" }
  ],
  authInfo: [
    { label: "API Key", value: "ak_xxxx_xxxx_7K92" },
    { label: "签名算法", value: "HMAC-SHA256" },
    { label: "最近调用时间", value: "2026-03-27 13:42" },
    { label: "日调用额度", value: "10,000 次 / 已使用 4,892 次" }
  ],
  callbackInfo: [
    { label: "回调地址", value: "https://erp.partner.com/callback" },
    { label: "通知事件", value: "任务成功、任务失败、回调失败" },
    { label: "超时阈值", value: "5 秒" },
    { label: "最近结果", value: "1 次超时重试后成功", tone: "warning" }
  ]
};

const taskDetail = {
  id: "TASK-20260327-0821",
  status: { text: "成功", tone: "success" },
  summary: [
    { label: "任务状态", value: "成功", tone: "success" },
    { label: "生成模式", value: "异步" },
    { label: "创建时间", value: "2026-03-27 09:20" },
    { label: "完成时间", value: "2026-03-27 09:21" },
    { label: "输入摘要", value: "开放平台结果获取接口，强调任务未完成与结果过期校验。" },
    { label: "失败原因", value: "无" }
  ],
  callback: [
    { label: "回调地址", value: "https://erp.partner.com/callback" },
    { label: "最终结果", value: "重试后成功", tone: "warning" },
    { label: "最近响应码", value: "200" },
    { label: "累计重试次数", value: "1" }
  ],
  timeline: [
    { title: "09:20:02 创建任务", text: "已完成鉴权、签名校验与参数合法性检查。" },
    { title: "09:20:11 进入处理中", text: "开始解析输入材料，加载标准模板和覆盖维度。" },
    { title: "09:21:04 生成成功", text: "输出 18 条测试用例，其中边界类 4 条、异常类 5 条。" }
  ]
};

const caseDetail = {
  id: "CASE-001",
  title: "任务完成后获取结果成功",
  priority: { text: "P0", tone: "danger" },
  type: { text: "正常", tone: "success" },
  info: [
    { label: "所属模块", value: "结果获取" },
    { label: "场景描述", value: "任务成功后，调用结果接口获取完整结构化测试用例集合。" },
    { label: "前置条件", value: "任务状态为成功，结果未过期，调用方具备归属权限。" },
    { label: "标签", value: "结果获取 / JSON / 权限校验" }
  ],
  steps: [
    "调用结果接口，传入合法任务 ID 与应用签名。",
    "校验响应状态码为 200，返回体包含 resultMeta、summary 和 cases。",
    "校验 cases 中每条用例含标题、前置条件、步骤、预期结果、优先级。",
    "校验返回体展示生成时间、模板信息与覆盖维度说明。"
  ],
  expected: "接口返回完整的结构化结果，字段齐全，任务归属合法，未出现“任务尚未完成”或“结果已过期”类错误信息。"
};

export async function fetchDashboardData() {
  await wait();
  return {
    hero: [
      { label: "接口可用率", value: "98.2%" },
      { label: "异步平均完成时间", value: "12.4s" },
      { label: "活跃应用数", value: "36" }
    ],
    stats: [
      { iconClass: "icon-blue", label: "今日总调用", value: "4,892", icon: "调" },
      { iconClass: "icon-green", label: "成功返回任务", value: "3,978", icon: "成" },
      { iconClass: "icon-orange", label: "进行中异步任务", value: "1,204", icon: "异" },
      { iconClass: "icon-red", label: "待处理失败告警", value: "57", icon: "错" }
    ]
  };
}

export async function fetchApps() {
  await wait();
  return appRows;
}

export async function fetchAppDetail() {
  await wait();
  return appDetail;
}

export async function fetchGeneratePageData() {
  await wait();
  return {
    requestDefaults: {
      appId: "APP_91KD28A",
      requestId: "REQ_20260327_092001",
      title: "开放平台生成任务结果获取接口",
      mode: "异步",
      template: "标准模板",
      material: "接口需支持按任务 ID 拉取生成结果，并在任务未完成时返回明确错误信息。"
    },
    coverageOptions: ["正常", "异常", "边界", "权限", "兼容"],
    previewBlocks: [
      { title: "resultMeta", text: "taskId、mode、template、generatedAt" },
      { title: "summary", text: "caseCount、coverage、expiredAt" },
      { title: "cases[]", text: "title、steps、expectedResult、priority" },
      { title: "partialFailures", text: "errorCode、reason、retryable" }
    ]
  };
}

export async function fetchTaskDetail() {
  await wait();
  return taskDetail;
}

export async function fetchResults() {
  await wait();
  return resultRows;
}

export async function fetchCaseDetail() {
  await wait();
  return caseDetail;
}
