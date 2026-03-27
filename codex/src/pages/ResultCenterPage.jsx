import { useCallback } from "react";
import { Link } from "react-router-dom";
import PageHeader from "../components/PageHeader";
import DataTable from "../components/DataTable";
import useAsyncData from "../hooks/useAsyncData";
import { fetchResults } from "../api/mockApi";

export default function ResultCenterPage() {
  const loader = useCallback(() => fetchResults(), []);
  const { data: resultRows, loading } = useAsyncData(loader, []);

  if (loading) {
    return <div className="loading-card">正在加载结果列表...</div>;
  }

  return (
    <div className="page-content">
      <PageHeader
        title="结果中心"
        subtitle="保留筛选、列表和详情跳转，方便后续替换成真实结果接口。"
        actions={<><button className="btn btn-default">下载结果文件</button><button className="btn btn-primary">查看用例详情</button></>}
      />
      <section className="toolbar">
        <div className="toolbar-left">
          <div className="field"><label>优先级</label><select className="field-select"><option>全部</option><option>P0</option><option>P1</option></select></div>
          <div className="field"><label>场景标签</label><select className="field-select"><option>全部场景</option><option>结果获取</option></select></div>
          <div className="field"><label>覆盖类型</label><select className="field-select"><option>全部类型</option><option>正常</option><option>异常</option><option>边界</option></select></div>
        </div>
        <div className="toolbar-right"><button className="btn btn-default">重置</button><button className="btn btn-primary">查询</button></div>
      </section>
      <section className="table-card">
        <div className="card-title-row"><h2 className="card-title">测试用例列表</h2><span className="tag tag-success">共 {resultRows.length} 条</span></div>
        <DataTable
          columns={[
            { key: "caseId", title: "caseId" },
            { key: "title", title: "标题" },
            { key: "scenario", title: "场景" },
            { key: "priority", title: "优先级", render: (row) => <span className={`tag tag-${row.priorityTone}`}>{row.priority}</span> },
            { key: "type", title: "用例类型", render: (row) => <span className={`tag tag-${row.typeTone}`}>{row.type}</span> },
            { key: "tags", title: "标签" }
          ]}
          rows={resultRows}
          renderActions={(row) => (
            <>
              <Link to={`/results/${row.caseId}`}>查看详情</Link>
              <button className="btn btn-link">复制链接</button>
            </>
          )}
        />
      </section>
    </div>
  );
}
