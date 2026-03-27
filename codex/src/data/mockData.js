export const navGroups = [
  {
    title: "总览",
    items: [{ label: "监控工作台", icon: "◉", to: "/dashboard" }]
  },
  {
    title: "开放接入",
    items: [
      { label: "接入管理", icon: "◎", to: "/apps" },
      { label: "应用详情", icon: "·", to: "/apps/APP_91KD28A", indent: true }
    ]
  },
  {
    title: "生成服务",
    items: [
      { label: "生成工作台", icon: "◆", to: "/generate" },
      { label: "任务详情", icon: "◇", to: "/tasks/TASK-20260327-0821" },
      { label: "结果中心", icon: "▣", to: "/results" },
      { label: "用例详情", icon: "·", to: "/results/CASE-001", indent: true }
    ]
  }
];

export const appRows = [
  {
    name: "CaseGen-ERP",
    id: "APP_91KD28A",
    status: "启用",
    statusTone: "success",
    callback: "https://erp.partner.com/callback",
    contact: "刘洋",
    createdAt: "2026-03-22 10:40"
  },
  {
    name: "QA-Partner",
    id: "APP_18KF93M",
    status: "冻结",
    statusTone: "warning",
    callback: "未配置",
    contact: "王敏",
    createdAt: "2026-03-20 18:25"
  },
  {
    name: "Flow-TestHub",
    id: "APP_71PS88Q",
    status: "启用",
    statusTone: "info",
    callback: "https://hub.test.com/open/case",
    contact: "赵磊",
    createdAt: "2026-03-18 09:10"
  }
];

export const resultRows = [
  {
    caseId: "CASE-001",
    title: "任务完成后获取结果成功",
    scenario: "结果获取",
    priority: "P0",
    priorityTone: "danger",
    type: "正常",
    typeTone: "success",
    tags: "任务完成 / JSON"
  },
  {
    caseId: "CASE-006",
    title: "任务未完成时返回不可获取提示",
    scenario: "结果获取",
    priority: "P1",
    priorityTone: "warning",
    type: "异常",
    typeTone: "warning",
    tags: "任务处理中"
  },
  {
    caseId: "CASE-011",
    title: "结果过期后提示重新生成",
    scenario: "结果获取",
    priority: "P1",
    priorityTone: "warning",
    type: "边界",
    typeTone: "info",
    tags: "过期校验"
  }
];

export const notifications = [
  { text: "CaseGen-ERP 异步任务成功率下降至 92%", time: "2 分钟前", unread: true },
  { text: "有 1 个应用等待补全回调配置", time: "18 分钟前", unread: true },
  { text: "本周模板下载量较上周提升 16%", time: "1 小时前", unread: false }
];
