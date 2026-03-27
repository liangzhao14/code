import { useCallback } from "react";
import PageHeader from "../components/PageHeader";
import DetailGrid from "../components/DetailGrid";
import useAsyncData from "../hooks/useAsyncData";
import { fetchCaseDetail } from "../api/mockApi";

export default function CaseDetailPage() {
  const loader = useCallback(() => fetchCaseDetail(), []);
  const { data, loading } = useAsyncData(loader, { priority: {}, type: {}, info: [], steps: [], expected: "" });

  if (loading) {
    return <div className="loading-card">正在加载用例详情...</div>;
  }

  return (
    <div className="page-content">
      <PageHeader
        title={`${data.id} / ${data.title}`}
        subtitle="单条用例详情页已拆成 React 结构，后续可直接接结果详情接口。"
        actions={<><span className={`tag tag-${data.priority.tone}`}>{data.priority.text}</span><span className={`tag tag-${data.type.tone}`}>{data.type.text}</span><button className="btn btn-default">复制用例</button></>}
      />
      <section className="detail-card">
        <div className="card-title-row"><h2 className="card-title">用例信息</h2></div>
        <DetailGrid items={data.info} />
      </section>
      <section className="detail-card">
        <div className="card-title-row"><h2 className="card-title">测试步骤</h2></div>
        <ol className="plain-list">
          {data.steps.map((step) => <li key={step}>{step}</li>)}
        </ol>
      </section>
      <section className="detail-card">
        <div className="card-title-row"><h2 className="card-title">预期结果</h2></div>
        <div className="notice-box">{data.expected}</div>
      </section>
    </div>
  );
}
