import { useCallback, useState } from "react";
import { Link } from "react-router-dom";
import PageHeader from "../components/PageHeader";
import { Modal } from "../components/Overlay";
import DataTable from "../components/DataTable";
import useAsyncData from "../hooks/useAsyncData";
import { fetchApps } from "../api/mockApi";

export default function AppAccessPage() {
  const [showCreate, setShowCreate] = useState(false);
  const [showReset, setShowReset] = useState(false);
  const loader = useCallback(() => fetchApps(), []);
  const { data: appRows, loading } = useAsyncData(loader, []);

  if (loading) {
    return <div className="loading-card">正在加载接入应用列表...</div>;
  }

  return (
    <div className="page-content">
      <PageHeader
        title="接入管理"
        subtitle="React 版接入应用列表页，保留新建应用和重置密钥两个核心覆盖层。"
        actions={
          <>
            <button className="btn btn-default">导出清单</button>
            <button className="btn btn-primary" onClick={() => setShowCreate(true)}>新建接入应用</button>
          </>
        }
      />
      <section className="toolbar">
        <div className="toolbar-left">
          <div className="field"><label>应用名称</label><input className="field-input" placeholder="请输入应用名称" /></div>
          <div className="field"><label>应用状态</label><select className="field-select"><option>全部状态</option><option>启用</option><option>冻结</option></select></div>
          <div className="field"><label>回调配置</label><select className="field-select"><option>全部</option><option>已配置</option><option>待配置</option></select></div>
        </div>
        <div className="toolbar-right">
          <button className="btn btn-default">重置</button>
          <button className="btn btn-primary">查询</button>
        </div>
      </section>
      <section className="table-card">
        <div className="card-title-row"><h2 className="card-title">接入应用列表</h2><span className="tag tag-info">总数 {appRows.length}</span></div>
        <DataTable
          columns={[
            { key: "name", title: "应用名称" },
            { key: "id", title: "应用标识" },
            { key: "status", title: "状态", render: (row) => <span className={`tag tag-${row.statusTone}`}>{row.status}</span> },
            { key: "callback", title: "回调地址" },
            { key: "contact", title: "联系人" },
            { key: "createdAt", title: "创建时间" }
          ]}
          rows={appRows}
          renderActions={(row) => (
            <>
              <Link to={`/apps/${row.id}`}>查看详情</Link>
              <button className="btn btn-link" onClick={() => setShowReset(true)}>重置密钥</button>
            </>
          )}
        />
      </section>
      <Modal
        title="新建接入应用"
        open={showCreate}
        onClose={() => setShowCreate(false)}
        footer={<><button className="btn btn-default" onClick={() => setShowCreate(false)}>取消</button><button className="btn btn-primary" onClick={() => setShowCreate(false)}>创建应用</button></>}
      >
        <div className="overlay-grid">
          <div className="field"><label>应用名称 *</label><input className="field-input" placeholder="如：CaseGen-ERP" /></div>
          <div className="field"><label>回调地址</label><input className="field-input" placeholder="https://example.com/callback" /></div>
          <div className="field"><label>联系人</label><input className="field-input" placeholder="请输入联系人" /></div>
          <div className="field"><label>用途说明</label><textarea className="field-textarea" placeholder="说明接入系统用途与业务场景" /></div>
          <div className="warn-box">应用名称在同一租户内必须唯一，回调地址需符合允许协议与域名规则。</div>
        </div>
      </Modal>
      <Modal
        title="重置密钥确认"
        open={showReset}
        onClose={() => setShowReset(false)}
        widthClass="modal-confirm"
        footer={<><button className="btn btn-default" onClick={() => setShowReset(false)}>取消</button><button className="btn btn-danger" onClick={() => setShowReset(false)}>确认重置</button></>}
      >
        <div className="warn-box">重置后旧密钥将立即失效，调用方必须重新保存并更新到业务系统配置中。</div>
      </Modal>
    </div>
  );
}
