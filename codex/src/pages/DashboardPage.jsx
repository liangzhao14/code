import { useCallback } from "react";
import { Link } from "react-router-dom";
import PageHeader from "../components/PageHeader";
import useAsyncData from "../hooks/useAsyncData";
import { fetchDashboardData } from "../api/mockApi";

export default function DashboardPage() {
  const loader = useCallback(() => fetchDashboardData(), []);
  const { data, loading } = useAsyncData(loader, { hero: [], stats: [] });

  if (loading) {
    return <div className="loading-card">正在加载监控首页数据...</div>;
  }

  return (
    <div className="page-content">
      <PageHeader
        title="测试用例生成开放服务监控台"
        subtitle="将 PRD 中的开放接入、生成服务、任务管理与运营保障整理成一个可继续开发的 React 首页。"
        actions={<span className="tag tag-info">React 路由首页</span>}
      />
      <section className="hero-banner">
        <div>
          <h2 className="page-title">开放平台总览</h2>
          <p className="page-subtitle">聚焦调用量、异步履约、失败趋势和热点模板，方便后续接入真实接口后替换 mock 数据。</p>
          <div className="hero-chip-row">
            <span className="chip">今日调用量 4,892</span>
            <span className="chip">异步任务占比 68%</span>
            <span className="chip">失败任务需人工排查 9 个</span>
          </div>
        </div>
        <div className="route-card-grid">
          {data.hero.map((item) => (
            <div className="section-card" key={item.label}><div className="stat-value">{item.value}</div><div className="stat-label">{item.label}</div></div>
          ))}
        </div>
      </section>
      <section className="stat-bar">
        {data.stats.map((item) => (
          <div className="stat-card" key={item.label}>
            <div className={`stat-icon ${item.iconClass}`}>{item.icon}</div>
            <div className="stat-info"><div className="stat-value">{item.value}</div><div className="stat-label">{item.label}</div></div>
          </div>
        ))}
      </section>
      <section className="grid-2">
        <div className="section-card">
          <div className="card-title-row"><h2 className="card-title">热点入口</h2><span className="tag tag-success">可继续细化</span></div>
          <div className="summary-list">
            <div className="summary-item"><strong>接入管理</strong><p className="page-subtitle">管理第三方应用、回调地址和密钥生命周期。</p><Link to="/apps">打开页面</Link></div>
            <div className="summary-item"><strong>生成工作台</strong><p className="page-subtitle">发起同步或异步生成任务，补充结构化规则。</p><Link to="/generate">打开页面</Link></div>
            <div className="summary-item"><strong>结果中心</strong><p className="page-subtitle">查看用例结果、筛选优先级和导出结果文件。</p><Link to="/results">打开页面</Link></div>
          </div>
        </div>
        <div className="section-card">
          <div className="card-title-row"><h2 className="card-title">待办清单</h2><span className="tag tag-warning">Mock 数据</span></div>
          <table>
            <thead><tr><th>事项</th><th>对象</th><th>优先级</th><th>操作</th></tr></thead>
            <tbody>
              <tr><td>回调超时连续 3 次</td><td>CaseGen-ERP</td><td><span className="tag tag-danger">高</span></td><td><Link to="/tasks/TASK-20260327-0821">查看任务</Link></td></tr>
              <tr><td>等待补全联系人信息</td><td>QA-Partner</td><td><span className="tag tag-warning">中</span></td><td><Link to="/apps/APP_91KD28A">查看应用</Link></td></tr>
              <tr><td>结果即将过期</td><td>TASK-20260327-0821</td><td><span className="tag tag-info">提醒</span></td><td><Link to="/results">查看结果</Link></td></tr>
            </tbody>
          </table>
        </div>
      </section>
    </div>
  );
}
