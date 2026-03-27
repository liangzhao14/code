import { useCallback } from "react";
import PageHeader from "../components/PageHeader";
import DetailGrid from "../components/DetailGrid";
import useAsyncData from "../hooks/useAsyncData";
import { fetchTaskDetail } from "../api/mockApi";

export default function TaskDetailPage() {
  const loader = useCallback(() => fetchTaskDetail(), []);
  const { data, loading } = useAsyncData(loader, { status: {}, summary: [], callback: [], timeline: [] });

  if (loading) {
    return <div className="loading-card">正在加载任务详情...</div>;
  }

  return (
    <div className="page-content">
      <PageHeader
        title={`任务详情 / ${data.id}`}
        subtitle="任务状态、输入摘要、回调状态和时间线已经拆成 React 页面结构。"
        actions={<><span className={`tag tag-${data.status.tone}`}>{data.status.text}</span><button className="btn btn-default">刷新状态</button><button className="btn btn-primary">查看结果</button></>}
      />
      <section className="grid-2">
        <div className="detail-card">
          <div className="card-title-row"><h2 className="card-title">任务摘要</h2></div>
          <DetailGrid items={data.summary} />
        </div>
        <div className="detail-card">
          <div className="card-title-row"><h2 className="card-title">回调状态</h2></div>
          <DetailGrid items={data.callback} />
        </div>
      </section>
      <section className="detail-card">
        <div className="card-title-row"><h2 className="card-title">状态流转时间线</h2><span className="tag tag-info">待处理 → 处理中 → 成功</span></div>
        <div className="summary-list">
          {data.timeline.map((item) => (
            <div className="summary-item" key={item.title}><strong>{item.title}</strong><p className="page-subtitle">{item.text}</p></div>
          ))}
        </div>
      </section>
    </div>
  );
}
