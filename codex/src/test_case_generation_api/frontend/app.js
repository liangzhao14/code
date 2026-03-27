const state = {
  route: "dashboard",
  routeId: null,
  overview: null,
  apps: [],
  tasks: [],
  results: [],
  search: "",
  coverage: new Set(["normal", "boundary", "exception"]),
  secrets: loadSecrets(),
  modal: null,
};

const pageTitle = document.getElementById("pageTitle");
const breadcrumb = document.getElementById("breadcrumb");
const appRoot = document.getElementById("app");
const modalRoot = document.getElementById("modalRoot");
const toastElement = document.getElementById("toast");

document.getElementById("refreshButton").addEventListener("click", () => refreshData());
document.getElementById("globalSearch").addEventListener("input", (event) => {
  state.search = event.target.value.trim().toLowerCase();
  render();
});

document.querySelectorAll(".nav-link").forEach((button) => {
  button.addEventListener("click", () => {
    location.hash = `#/${button.dataset.route}`;
  });
});

window.addEventListener("hashchange", syncRouteFromHash);
document.addEventListener("click", handleDocumentClick);
document.addEventListener("submit", handleDocumentSubmit);

syncRouteFromHash();
refreshData();

async function refreshData() {
  try {
    const [overview, apps, tasks, results] = await Promise.all([
      fetchJson("/api/v1/console/overview"),
      fetchJson("/api/v1/console/apps"),
      fetchJson("/api/v1/console/tasks"),
      fetchJson("/api/v1/console/results"),
    ]);
    state.overview = overview.data;
    state.apps = apps.data;
    state.tasks = tasks.data;
    state.results = results.data;
    render();
  } catch (error) {
    showToast(error.message || "数据刷新失败");
  }
}

function syncRouteFromHash() {
  const raw = location.hash.replace(/^#\/?/, "");
  const parts = raw ? raw.split("/") : ["dashboard"];
  state.route = parts[0] || "dashboard";
  state.routeId = parts[1] || null;
  document.querySelectorAll(".nav-link").forEach((button) => {
    button.classList.toggle("active", button.dataset.route === state.route);
  });
  render();
}

function render() {
  const meta = routeMeta();
  pageTitle.textContent = meta.title;
  breadcrumb.textContent = meta.breadcrumb;
  appRoot.innerHTML = renderPage();
  renderModal();
}

function routeMeta() {
  switch (state.route) {
    case "apps":
      return state.routeId
        ? { title: "应用详情", breadcrumb: "首页 / 开放接入 / 应用详情" }
        : { title: "接入管理", breadcrumb: "首页 / 开放接入 / 接入管理" };
    case "generate":
      return { title: "生成工作台", breadcrumb: "首页 / 生成服务 / 生成工作台" };
    case "tasks":
      return { title: "任务详情", breadcrumb: "首页 / 生成服务 / 任务详情" };
    case "results":
      return { title: "结果中心", breadcrumb: "首页 / 生成服务 / 结果中心" };
    case "cases":
      return { title: "用例详情", breadcrumb: "首页 / 生成服务 / 用例详情" };
    default:
      return { title: "监控工作台", breadcrumb: "首页 / 监控工作台" };
  }
}

function renderPage() {
  switch (state.route) {
    case "apps":
      return state.routeId ? renderAppDetailPage() : renderAppsPage();
    case "generate":
      return renderGeneratePage();
    case "tasks":
      return renderTasksPage();
    case "results":
      return renderResultsPage();
    case "cases":
      return renderCaseDetailPage();
    default:
      return renderDashboardPage();
  }
}

function renderDashboardPage() {
  const summary = state.overview?.summary || {};
  const recentTasks = applySearch(state.overview?.recent_tasks || [], ["title", "request_id", "app_name"]);
  const topApps = applySearch(state.overview?.top_apps || [], ["name"]);
  const events = applySearch(state.overview?.recent_events || [], ["event_type", "app_id"]);
  return `
    <section class="stat-grid">
      ${renderStatCard("接入应用", summary.app_count ?? 0, "当前进程内的应用数")}
      ${renderStatCard("生成任务", summary.task_count ?? 0, `成功率 ${summary.success_rate ?? 0}%`)}
      ${renderStatCard("测试用例", summary.case_count ?? 0, `失败任务 ${summary.failed_count ?? 0}`)}
      ${renderStatCard("审计事件", summary.audit_event_count ?? 0, `处理中 ${summary.processing_count ?? 0}`)}
    </section>
    <section class="grid-two">
      <article class="surface-card">
        <div class="surface-header">
          <div>
            <h2 class="section-title">最近任务</h2>
            <div class="muted">覆盖同步与异步生成状态</div>
          </div>
          <div class="btn-row">
            <button class="btn btn-default" data-route-link="tasks">查看全部</button>
            <button class="btn btn-primary" data-route-link="generate">发起生成</button>
          </div>
        </div>
        ${recentTasks.length ? renderTaskTable(recentTasks.slice(0, 6), false) : renderEmpty("还没有生成任务", "先创建应用并提交一次生成请求，工作台数据就会丰富起来。")}
      </article>
      <article class="surface-card">
        <div class="surface-header">
          <div>
            <h2 class="section-title">应用热度</h2>
            <div class="muted">按任务量排序的应用视图</div>
          </div>
        </div>
        ${
          topApps.length
            ? `<div class="metric-list">${topApps
                .map((item, index) => `<div class="metric-row"><span>${index + 1}. <button class="btn-link" data-route-link="apps/${item.app_id}">${escapeHtml(item.name)}</button></span><strong>${item.task_count}</strong></div>`)
                .join("")}</div>`
            : renderEmpty("暂无热度数据", "提交任务后会自动形成应用排名。")
        }
      </article>
    </section>
    <article class="surface-card">
      <div class="surface-header">
        <div>
          <h2 class="section-title">审计事件流</h2>
          <div class="muted">方便快速确认创建、生成、重试等动作</div>
        </div>
      </div>
      ${
        events.length
          ? `<div class="timeline">${events
              .map((event) => `<div class="timeline-item"><div class="timeline-time">${formatTime(event.created_at)}</div><div class="timeline-body"><strong>${escapeHtml(event.event_type)}</strong><div class="muted">应用: ${escapeHtml(event.app_id || "system")}</div><div>${escapeHtml(JSON.stringify(event.detail))}</div></div></div>`)
              .join("")}</div>`
          : renderEmpty("还没有审计事件", "当前控制台会在创建应用、提交任务和重试失败任务时自动记录事件。")
      }
    </article>
  `;
}

function renderAppsPage() {
  const apps = applySearch(state.apps, ["name", "app_id", "callback_url", "contact"]);
  return `
    <section class="surface-card">
      <div class="surface-header">
        <div>
          <h2 class="section-title">接入应用列表</h2>
          <div class="muted">支持新建、查看详情和重置密钥。</div>
        </div>
        <div class="btn-row">
          <button class="btn btn-default" data-action="export-apps">导出清单</button>
          <button class="btn btn-primary" data-action="open-create-app">新建接入应用</button>
        </div>
      </div>
      ${apps.length ? renderAppsTable(apps) : renderEmpty("还没有接入应用", "先创建一个应用，再在生成工作台中用它发起测试用例生成。")}
    </section>
  `;
}

function renderAppDetailPage() {
  const app = state.apps.find((item) => item.app_id === state.routeId);
  if (!app) {
    return renderEmpty("应用不存在", "返回接入管理页重新选择一个应用。");
  }
  const tasks = state.tasks.filter((task) => task.app_id === app.app_id).slice(0, 5);
  return `
    <section class="surface-card">
      <div class="surface-header">
        <div>
          <h2 class="section-title">${escapeHtml(app.name)}</h2>
          <div class="muted">${escapeHtml(app.description || "未填写应用说明")}</div>
        </div>
        <div class="detail-actions">
          <button class="btn btn-default" data-route-link="apps">返回列表</button>
          <button class="btn btn-primary" data-route-link="generate">用此应用生成</button>
          <button class="btn btn-danger" data-action="reset-secret" data-app-id="${app.app_id}">重置密钥</button>
        </div>
      </div>
      <div class="detail-grid">
        ${renderDetailItem("应用标识", app.app_id)}
        ${renderDetailItem("Key ID", app.api_key_id)}
        ${renderDetailItem("回调地址", app.callback_url || "未配置")}
        ${renderDetailItem("联系人", app.contact || "未填写")}
        ${renderDetailItem("创建时间", formatTime(app.created_at))}
        ${renderDetailItem("本地密钥状态", state.secrets[app.app_id] ? "当前浏览器已保存，可直接发起签名请求" : "未保存，仅能查看只读数据")}
      </div>
      <div class="grid-two">
        <article class="surface-card">
          <h3 class="section-title">签名调用示意</h3>
          <div class="code-block">${escapeHtml(renderSignatureSnippet(app))}</div>
        </article>
        <article class="surface-card">
          <h3 class="section-title">最近任务</h3>
          ${tasks.length ? renderTaskTable(tasks, false) : renderEmpty("这个应用还没有任务", "可以直接去生成工作台发起第一条请求。")}
        </article>
      </div>
    </section>
  `;
}

function renderGeneratePage() {
  const options = state.apps.map((app) => `<option value="${app.app_id}">${escapeHtml(app.name)}${state.secrets[app.app_id] ? " · 已保存密钥" : ""}</option>`).join("");
  return `
    <section class="grid-two">
      <article class="surface-card">
        <div class="surface-header">
          <div>
            <h2 class="section-title">发起测试用例生成</h2>
            <div class="muted">直接对接现有生成接口，并在浏览器端完成 HMAC 签名。</div>
          </div>
        </div>
        ${
          state.apps.length
            ? `
              <form id="generateForm" class="form-grid">
                <div class="field">
                  <label>接入应用</label>
                  <select class="field-select" name="app_id" required>
                    <option value="">请选择应用</option>
                    ${options}
                  </select>
                  <div class="field-tip">只有当前浏览器已保存密钥的应用才能直接发起生成。</div>
                </div>
                <div class="field">
                  <label>请求流水号</label>
                  <input class="field-input" name="request_id" value="req-${Date.now()}" required>
                </div>
                <div class="field">
                  <label>标题</label>
                  <input class="field-input" name="title" placeholder="例如：登录 API 回归" required>
                </div>
                <div class="field">
                  <label>生成模式</label>
                  <select class="field-select" name="generation_mode">
                    <option value="sync">同步</option>
                    <option value="async">异步</option>
                  </select>
                </div>
                <div class="field" style="grid-column: 1 / -1;">
                  <label>需求描述</label>
                  <textarea class="field-textarea" name="description" placeholder="输入业务背景、接口行为、关键约束和重点风险点" required></textarea>
                </div>
                <div class="field">
                  <label>模板 ID</label>
                  <input class="field-input" name="template_id" value="standard">
                </div>
                <div class="field">
                  <label>结构化规则</label>
                  <textarea class="field-textarea" name="structured_rules" placeholder="每行一条，例如：返回结果必须是 JSON"></textarea>
                </div>
                <div class="field" style="grid-column: 1 / -1;">
                  <label>覆盖维度</label>
                  <div class="chip-group">
                    ${["normal", "boundary", "exception", "security", "compatibility"]
                      .map((item) => `<label class="chip ${state.coverage.has(item) ? "active" : ""}"><input type="checkbox" name="coverage_dimension" value="${item}" ${state.coverage.has(item) ? "checked" : ""} hidden>${item}</label>`)
                      .join("")}
                  </div>
                </div>
                <div class="field" style="grid-column: 1 / -1;">
                  <label>附件引用</label>
                  <textarea class="field-textarea" name="attachments" placeholder="每行使用 type|name|url，例如：prd|登录需求|https://example.com/prd"></textarea>
                </div>
                <div class="btn-row" style="grid-column: 1 / -1; justify-content: flex-end;">
                  <button type="button" class="btn btn-default" data-action="fill-demo-request">填充示例</button>
                  <button type="submit" class="btn btn-primary">生成测试用例</button>
                </div>
              </form>
            `
            : renderEmpty("请先创建应用", "生成请求依赖接入应用和本地保存的密钥。你可以先到接入管理中创建一个应用。")
        }
      </article>
      <article class="surface-card">
        <div class="surface-header">
          <div>
            <h2 class="section-title">发起前提示</h2>
            <div class="muted">与现有 API 能力的真实边界保持一致</div>
          </div>
        </div>
        <div class="metric-list">
          <div class="metric-row"><span>鉴权方式</span><strong>HMAC-SHA256</strong></div>
          <div class="metric-row"><span>时效窗口</span><strong>5 分钟</strong></div>
          <div class="metric-row"><span>默认限流</span><strong>60 次/分钟/应用</strong></div>
          <div class="metric-row"><span>结果落点</span><strong>任务详情 + 结果中心</strong></div>
        </div>
        <div class="notice">如果选中的应用没有本地保存密钥，控制台会阻止发起请求。这与后端不会重复返回明文密钥的安全策略一致。</div>
      </article>
    </section>
  `;
}

function renderTasksPage() {
  const tasks = applySearch(state.tasks, ["title", "request_id", "app_name", "task_id"]);
  const detail = state.routeId ? state.tasks.find((task) => task.task_id === state.routeId) : tasks[0];
  return `
    <section class="surface-card">
      <div class="surface-header">
        <div>
          <h2 class="section-title">任务列表</h2>
          <div class="muted">支持查看状态，并对失败任务发起重试。</div>
        </div>
      </div>
      ${tasks.length ? renderTaskTable(tasks, true) : renderEmpty("暂无任务", "去生成工作台提交一个请求后，这里会出现完整的任务轨迹。")}
    </section>
    ${
      detail
        ? `<section class="surface-card">
            <div class="surface-header">
              <div>
                <h2 class="section-title">任务详情</h2>
                <div class="muted">${escapeHtml(detail.task_id)}</div>
              </div>
              <div class="btn-row">
                <button class="btn btn-default" data-action="copy-task" data-task-id="${detail.task_id}">复制任务 ID</button>
                ${detail.status === "failed" ? `<button class="btn btn-danger" data-action="retry-task" data-task-id="${detail.task_id}" data-app-id="${detail.app_id}">重试任务</button>` : ""}
              </div>
            </div>
            <div class="detail-grid">
              ${renderDetailItem("应用", `${detail.app_name} (${detail.app_id})`)}
              ${renderDetailItem("请求流水号", detail.request_id)}
              ${renderDetailItem("生成模式", detail.generation_mode)}
              ${renderDetailItem("状态", statusTag(detail.status))}
              ${renderDetailItem("覆盖维度", detail.coverage_dimensions.join(", ") || "默认")}
              ${renderDetailItem("结果数量", String(detail.case_count))}
              ${renderDetailItem("创建时间", formatTime(detail.created_at))}
              ${renderDetailItem("更新时间", formatTime(detail.updated_at))}
            </div>
            <div class="code-block">${escapeHtml(detail.description)}</div>
            ${detail.error_message ? `<div class="notice"><strong>失败原因</strong><div>${escapeHtml(detail.error_message)}</div></div>` : ""}
          </section>`
        : ""
    }
  `;
}

function renderResultsPage() {
  const results = applySearch(state.results, ["title", "scenario", "app_name", "case_id", "task_id"]);
  return `
    <section class="surface-card">
      <div class="surface-header">
        <div>
          <h2 class="section-title">结果中心</h2>
          <div class="muted">汇总所有成功任务产出的结构化用例，可跳转到单条用例详情。</div>
        </div>
        <button class="btn btn-default" data-action="download-results">导出 JSON</button>
      </div>
      ${
        results.length
          ? `<div class="table-wrap">
              <table>
                <thead><tr><th>用例标题</th><th>应用</th><th>任务</th><th>覆盖维度</th><th>优先级</th><th>更新时间</th><th>操作</th></tr></thead>
                <tbody>
                  ${results.map((item) => `<tr><td>${escapeHtml(item.title)}</td><td>${escapeHtml(item.app_name)}</td><td>${escapeHtml(item.task_id)}</td><td>${statusTag(item.coverage_dimension, "info")}</td><td>${escapeHtml(item.priority)}</td><td>${formatTime(item.updated_at)}</td><td><button class="btn-link" data-route-link="cases/${item.case_id}">查看用例</button></td></tr>`).join("")}
                </tbody>
              </table>
            </div>`
          : renderEmpty("暂无结果", "成功任务产生的测试用例会自动汇总到这里。")
      }
    </section>
  `;
}

function renderCaseDetailPage() {
  const record = state.results.find((item) => item.case_id === state.routeId);
  if (!record) {
    return renderEmpty("找不到用例", "请从结果中心重新进入。");
  }
  const task = state.tasks.find((item) => item.task_id === record.task_id);
  return `
    <section class="surface-card">
      <div class="surface-header">
        <div>
          <h2 class="section-title">${escapeHtml(record.title)}</h2>
          <div class="muted">${escapeHtml(record.case_id)} · 来自 ${escapeHtml(record.app_name)}</div>
        </div>
        <div class="btn-row">
          <button class="btn btn-default" data-route-link="results">返回结果中心</button>
          <button class="btn btn-primary" data-action="copy-case" data-case-id="${record.case_id}">复制 JSON</button>
        </div>
      </div>
      <div class="detail-grid">
        ${renderDetailItem("所属任务", record.task_id)}
        ${renderDetailItem("覆盖维度", record.coverage_dimension)}
        ${renderDetailItem("优先级", record.priority)}
        ${renderDetailItem("更新时间", formatTime(record.updated_at))}
      </div>
      <div class="grid-two">
        <article class="surface-card">
          <h3 class="section-title">场景说明</h3>
          <div class="code-block">${escapeHtml(record.scenario)}</div>
          ${task ? `<div class="notice"><strong>任务输入摘要</strong><div>${escapeHtml(task.description)}</div></div>` : ""}
        </article>
        <article class="surface-card">
          <h3 class="section-title">结构化详情</h3>
          <div class="code-block">${escapeHtml(JSON.stringify(record, null, 2))}</div>
        </article>
      </div>
    </section>
  `;
}

function renderAppsTable(apps) {
  return `
    <div class="table-wrap">
      <table>
        <thead><tr><th>应用名称</th><th>应用标识</th><th>回调地址</th><th>联系人</th><th>任务数</th><th>创建时间</th><th>操作</th></tr></thead>
        <tbody>
          ${apps.map((app) => `<tr><td>${escapeHtml(app.name)}</td><td>${escapeHtml(app.app_id)}</td><td>${escapeHtml(app.callback_url || "未配置")}</td><td>${escapeHtml(app.contact || "未填写")}</td><td>${app.task_count || 0}</td><td>${formatTime(app.created_at)}</td><td><div class="table-actions"><button class="btn-link" data-route-link="apps/${app.app_id}">查看详情</button><button class="btn-link" data-action="reset-secret" data-app-id="${app.app_id}">重置密钥</button></div></td></tr>`).join("")}
        </tbody>
      </table>
    </div>
  `;
}

function renderTaskTable(tasks, linkable) {
  return `
    <div class="table-wrap">
      <table>
        <thead><tr><th>任务标题</th><th>应用</th><th>请求流水号</th><th>状态</th><th>结果数</th><th>更新时间</th><th>操作</th></tr></thead>
        <tbody>
          ${tasks.map((task) => `<tr><td>${escapeHtml(task.title)}</td><td>${escapeHtml(task.app_name)}</td><td>${escapeHtml(task.request_id)}</td><td>${statusTag(task.status)}</td><td>${task.case_count}</td><td>${formatTime(task.updated_at)}</td><td><div class="table-actions"><button class="btn-link" data-route-link="tasks/${task.task_id}">${linkable ? "查看详情" : "查看任务"}</button>${task.status === "success" ? `<button class="btn-link" data-route-link="results">查看结果</button>` : ""}</div></td></tr>`).join("")}
        </tbody>
      </table>
    </div>
  `;
}

function renderStatCard(label, value, note) {
  return `<article class="stat-card"><div class="stat-label">${label}</div><div class="stat-value">${value}</div><div class="stat-note">${note}</div></article>`;
}

function renderDetailItem(label, value) {
  return `<div class="detail-item"><strong>${label}</strong><div>${value}</div></div>`;
}

function renderEmpty(title, description) {
  return `<div class="empty-state"><h3>${title}</h3><p>${description}</p></div>`;
}

function renderModal() {
  if (!state.modal) {
    modalRoot.innerHTML = "";
    return;
  }

  if (state.modal.type === "create-app") {
    modalRoot.innerHTML = `
      <div class="modal-mask">
        <div class="modal-card">
          <div class="modal-header">
            <div><h2 class="modal-title">新建接入应用</h2><div class="muted">创建完成后会返回明文密钥，并自动保存在当前浏览器。</div></div>
            <button class="btn btn-default" data-action="close-modal">关闭</button>
          </div>
          <form id="createAppForm" class="modal-body">
            <div class="form-grid">
              <div class="field"><label>应用名称</label><input class="field-input" name="name" required></div>
              <div class="field"><label>联系人</label><input class="field-input" name="contact"></div>
              <div class="field" style="grid-column: 1 / -1;"><label>回调地址</label><input class="field-input" name="callback_url" placeholder="https://example.com/callback"></div>
              <div class="field" style="grid-column: 1 / -1;"><label>应用说明</label><textarea class="field-textarea" name="description"></textarea></div>
            </div>
            <div class="modal-actions"><button type="button" class="btn btn-default" data-action="close-modal">取消</button><button type="submit" class="btn btn-primary">创建应用</button></div>
          </form>
        </div>
      </div>
    `;
    return;
  }

  if (state.modal.type === "secret-result") {
    modalRoot.innerHTML = `
      <div class="modal-mask">
        <div class="modal-card">
          <div class="modal-header">
            <div><h2 class="modal-title">密钥已更新</h2><div class="muted">这段密钥只会返回一次，控制台已经替你保存到浏览器。</div></div>
            <button class="btn btn-default" data-action="close-modal">关闭</button>
          </div>
          <div class="modal-body">
            <div class="detail-grid">${renderDetailItem("应用", escapeHtml(state.modal.payload.name))}${renderDetailItem("App ID", escapeHtml(state.modal.payload.app_id))}</div>
            <div class="code-block">${escapeHtml(state.modal.payload.api_secret)}</div>
            <div class="modal-actions"><button type="button" class="btn btn-default" data-action="close-modal">稍后</button><button type="button" class="btn btn-primary" data-action="copy-secret" data-secret="${encodeURIComponent(state.modal.payload.api_secret)}">复制密钥</button></div>
          </div>
        </div>
      </div>
    `;
  }
}

async function handleDocumentSubmit(event) {
  if (event.target.id === "createAppForm") {
    event.preventDefault();
    const payload = Object.fromEntries(new FormData(event.target).entries());
    try {
      const response = await fetchJson("/api/v1/apps", { method: "POST", body: JSON.stringify(payload) });
      saveSecret(response.data.app_id, response.data.api_secret);
      state.modal = { type: "secret-result", payload: response.data };
      await refreshData();
      showToast("应用创建成功");
    } catch (error) {
      showToast(error.message || "创建应用失败");
    }
    return;
  }

  if (event.target.id === "generateForm") {
    event.preventDefault();
    const formData = new FormData(event.target);
    const appId = String(formData.get("app_id") || "");
    const secret = state.secrets[appId];
    if (!secret) {
      showToast("当前浏览器没有保存该应用密钥，请先创建或重置密钥");
      return;
    }
    const payload = {
      request_id: String(formData.get("request_id") || "").trim(),
      title: String(formData.get("title") || "").trim(),
      description: String(formData.get("description") || "").trim(),
      generation_mode: String(formData.get("generation_mode") || "sync"),
      template_id: String(formData.get("template_id") || "standard").trim() || "standard",
      coverage_dimensions: formData.getAll("coverage_dimension"),
      structured_rules: parseMultiline(String(formData.get("structured_rules") || "")),
      attachments: parseAttachments(String(formData.get("attachments") || "")),
    };
    try {
      const timestamp = String(Math.floor(Date.now() / 1000));
      const nonce = `nonce-${crypto.randomUUID()}`;
      const signature = await buildSignature(secret, timestamp, nonce, payload);
      await fetchJson("/api/v1/tasks/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json; charset=utf-8",
          "X-App-Id": appId,
          "X-Timestamp": timestamp,
          "X-Nonce": nonce,
          "X-Signature": signature,
        },
        body: JSON.stringify(payload),
      });
      await refreshData();
      const latestTask = state.tasks.find((task) => task.request_id === payload.request_id);
      location.hash = latestTask ? `#/tasks/${latestTask.task_id}` : "#/tasks";
      showToast("生成请求已提交");
    } catch (error) {
      showToast(error.message || "生成请求失败");
    }
  }
}

async function handleDocumentClick(event) {
  const routeTarget = event.target.closest("[data-route-link]");
  if (routeTarget) {
    location.hash = `#/${routeTarget.dataset.routeLink}`;
    return;
  }

  const actionTarget = event.target.closest("[data-action]");
  if (!actionTarget) {
    return;
  }

  const { action } = actionTarget.dataset;
  if (action === "close-modal") {
    state.modal = null;
    renderModal();
    return;
  }
  if (action === "open-create-app") {
    state.modal = { type: "create-app" };
    renderModal();
    return;
  }
  if (action === "copy-secret") {
    await navigator.clipboard.writeText(decodeURIComponent(actionTarget.dataset.secret));
    showToast("密钥已复制");
    return;
  }
  if (action === "reset-secret") {
    try {
      const response = await fetchJson(`/api/v1/apps/${actionTarget.dataset.appId}/reset-secret`, { method: "POST" });
      saveSecret(response.data.app_id, response.data.api_secret);
      state.modal = { type: "secret-result", payload: response.data };
      await refreshData();
      showToast("密钥已重置");
    } catch (error) {
      showToast(error.message || "重置密钥失败");
    }
    return;
  }
  if (action === "retry-task") {
    const appId = actionTarget.dataset.appId;
    const secret = state.secrets[appId];
    if (!secret) {
      showToast("没有本地密钥，无法重试任务");
      return;
    }
    const payload = {};
    try {
      const timestamp = String(Math.floor(Date.now() / 1000));
      const nonce = `nonce-${crypto.randomUUID()}`;
      const signature = await buildSignature(secret, timestamp, nonce, payload);
      await fetchJson(`/api/v1/tasks/${actionTarget.dataset.taskId}/retry`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json; charset=utf-8",
          "X-App-Id": appId,
          "X-Timestamp": timestamp,
          "X-Nonce": nonce,
          "X-Signature": signature,
        },
        body: JSON.stringify(payload),
      });
      await refreshData();
      showToast("失败任务已重新提交");
    } catch (error) {
      showToast(error.message || "任务重试失败");
    }
    return;
  }
  if (action === "fill-demo-request") {
    const form = document.getElementById("generateForm");
    if (form) {
      form.elements.title.value = "登录 API 回归";
      form.elements.description.value = "根据登录接口的账号密码校验、错误提示和返回结构生成正常、边界与异常场景测试用例。";
      form.elements.structured_rules.value = "返回结果必须为 JSON\n失败场景要标注错误码与提示文案";
      form.elements.attachments.value = "prd|登录需求|https://example.com/prd/login";
      showToast("已填入一份示例请求");
    }
    return;
  }
  if (action === "copy-task") {
    await navigator.clipboard.writeText(actionTarget.dataset.taskId);
    showToast("任务 ID 已复制");
    return;
  }
  if (action === "copy-case") {
    const record = state.results.find((item) => item.case_id === actionTarget.dataset.caseId);
    if (record) {
      await navigator.clipboard.writeText(JSON.stringify(record, null, 2));
      showToast("用例 JSON 已复制");
    }
    return;
  }
  if (action === "download-results") {
    downloadJson("caseflow-results.json", state.results);
    return;
  }
  if (action === "export-apps") {
    downloadJson("caseflow-apps.json", state.apps);
  }
}

async function fetchJson(url, options = {}) {
  const response = await fetch(url, { headers: { ...(options.headers || {}) }, ...options });
  const payload = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(payload?.error?.message || payload?.message || "请求失败");
  }
  return payload;
}

function applySearch(records, keys) {
  if (!state.search) {
    return records;
  }
  return records.filter((record) => keys.some((key) => String(record[key] ?? "").toLowerCase().includes(state.search)));
}

function parseMultiline(value) {
  return value.split(/\r?\n/).map((item) => item.trim()).filter(Boolean);
}

function parseAttachments(value) {
  return parseMultiline(value).map((line) => {
    const [type = "", name = "", url = ""] = line.split("|").map((item) => item.trim());
    return { type, name, url };
  });
}

function renderSignatureSnippet(app) {
  return `POST /api/v1/tasks/generate
X-App-Id: ${app.app_id}
X-Timestamp: <epoch-second>
X-Nonce: <random-string>
X-Signature: HMAC_SHA256(api_secret, timestamp + "." + nonce + "." + canonical_json(body))`;
}

function statusTag(status, explicitClass) {
  const mapping = { success: "success", failed: "danger", processing: "warning", pending: "info", normal: "info", boundary: "warning", exception: "danger" };
  const tagClass = explicitClass || mapping[status] || "info";
  return `<span class="tag ${tagClass}">${escapeHtml(status)}</span>`;
}

function formatTime(value) {
  return value ? new Date(value).toLocaleString("zh-CN", { hour12: false }) : "-";
}

function showToast(message) {
  toastElement.textContent = message;
  toastElement.classList.add("show");
  window.clearTimeout(window.__caseflowToastTimer);
  window.__caseflowToastTimer = window.setTimeout(() => toastElement.classList.remove("show"), 2200);
}

function escapeHtml(value) {
  return String(value).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;");
}

function loadSecrets() {
  try {
    return JSON.parse(localStorage.getItem("caseflow-secrets") || "{}");
  } catch {
    return {};
  }
}

function saveSecret(appId, secret) {
  state.secrets[appId] = secret;
  localStorage.setItem("caseflow-secrets", JSON.stringify(state.secrets));
}

async function buildSignature(secret, timestamp, nonce, body) {
  const encoder = new TextEncoder();
  const key = await crypto.subtle.importKey("raw", encoder.encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const payload = `${timestamp}.${nonce}.${canonicalBody(body)}`;
  const signature = await crypto.subtle.sign("HMAC", key, encoder.encode(payload));
  return toBase64(new Uint8Array(signature));
}

function canonicalBody(body) {
  return JSON.stringify(sortKeys(body)).replace(/[^\x20-\x7E]/g, (char) =>
    `\\u${char.charCodeAt(0).toString(16).padStart(4, "0")}`
  );
}

function sortKeys(value) {
  if (Array.isArray(value)) {
    return value.map(sortKeys);
  }
  if (value && typeof value === "object") {
    return Object.keys(value).sort().reduce((accumulator, key) => {
      accumulator[key] = sortKeys(value[key]);
      return accumulator;
    }, {});
  }
  return value;
}

function toBase64(bytes) {
  let binary = "";
  bytes.forEach((item) => { binary += String.fromCharCode(item); });
  return btoa(binary);
}

function downloadJson(filename, data) {
  const blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  link.click();
  URL.revokeObjectURL(url);
  showToast("已开始下载");
}
