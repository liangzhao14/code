import { useCallback } from "react";
import PageHeader from "../components/PageHeader";
import DetailGrid from "../components/DetailGrid";
import useAsyncData from "../hooks/useAsyncData";
import { fetchAppDetail } from "../api/mockApi";

export default function AppDetailPage() {
  const loader = useCallback(() => fetchAppDetail(), []);
  const { data, loading } = useAsyncData(loader, { baseInfo: [], authInfo: [], callbackInfo: [], status: "" });

  if (loading) {
    return <div className="loading-card">正在加载应用详情...</div>;
  }

  return (
    <div className="page-content">
      <PageHeader
        title={data.name}
        subtitle="保留基础信息、鉴权信息、回调设置三块信息区，方便后续接真实接口。"
        actions={<><span className="tag tag-success">{data.status}</span><button className="btn btn-default">发起生成</button></>}
      />
      <section className="detail-card">
        <div className="card-title-row"><h2 className="card-title">基础信息</h2></div>
        <DetailGrid items={data.baseInfo} />
      </section>
      <section className="detail-card">
        <div className="card-title-row"><h2 className="card-title">鉴权信息</h2></div>
        <DetailGrid items={data.authInfo} />
      </section>
      <section className="detail-card">
        <div className="card-title-row"><h2 className="card-title">回调设置</h2></div>
        <DetailGrid items={data.callbackInfo} />
      </section>
    </div>
  );
}
