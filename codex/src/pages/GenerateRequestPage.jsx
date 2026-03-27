import { useCallback, useState } from "react";
import PageHeader from "../components/PageHeader";
import { Drawer, Modal } from "../components/Overlay";
import MultiSelect from "../components/MultiSelect";
import useAsyncData from "../hooks/useAsyncData";
import { fetchGeneratePageData } from "../api/mockApi";

export default function GenerateRequestPage() {
  const [showDrawer, setShowDrawer] = useState(false);
  const [showAttachment, setShowAttachment] = useState(false);
  const loader = useCallback(() => fetchGeneratePageData(), []);
  const { data, loading } = useAsyncData(loader, {
    requestDefaults: {},
    coverageOptions: [],
    previewBlocks: []
  });
  const [coverage, setCoverage] = useState(["正常", "异常"]);

  const toggleCoverage = (value) => {
    setCoverage((items) => (items.includes(value) ? items.filter((item) => item !== value) : [...items, value]));
  };

  if (loading) {
    return <div className="loading-card">正在加载生成工作台配置...</div>;
  }

  return (
    <div className="page-content">
      <PageHeader
        title="生成工作台"
        subtitle="把 HTML 设计稿转换成可维护的 React 状态页面，后续只需要替换表单提交和接口调用。"
        actions={
          <>
            <button className="btn btn-default" onClick={() => setShowDrawer(true)}>补充业务规则</button>
            <button className="btn btn-default" onClick={() => setShowAttachment(true)}>添加附件引用</button>
            <button className="btn btn-primary">生成测试用例</button>
          </>
        }
      />
      <section className="grid-2">
        <div className="section-card">
          <div className="card-title-row"><h2 className="card-title">请求参数</h2><span className="tag tag-info">表单状态已组件化</span></div>
          <div className="form-grid">
              <div className="field"><label>应用标识 *</label><input className="field-input" defaultValue="APP_91KD28A" /></div>
              <div className="field"><label>请求流水号 *</label><input className="field-input" defaultValue={data.requestDefaults.requestId} /></div>
              <div className="field"><label>业务标题 *</label><input className="field-input" defaultValue={data.requestDefaults.title} /></div>
              <div className="field"><label>生成模式 *</label><select className="field-select"><option>{data.requestDefaults.mode}</option><option>同步</option></select></div>
              <div className="field"><label>模板标识</label><select className="field-select"><option>{data.requestDefaults.template}</option><option>自定义字段模板</option></select></div>
              <div className="field"><label>覆盖维度</label><MultiSelect values={coverage} options={data.coverageOptions} onToggle={toggleCoverage} /></div>
              <div className="field"><label>输入材料 *</label><textarea className="field-textarea" defaultValue={data.requestDefaults.material} /></div>
            </div>
          </div>
        <div className="section-card">
          <div className="card-title-row"><h2 className="card-title">返回结构预览</h2><span className="tag tag-success">Mock 结构</span></div>
          <div className="file-tile-grid">
            {data.previewBlocks.map((block) => (
              <div className="file-tile" key={block.title}><strong>{block.title}</strong><p className="page-subtitle">{block.text}</p></div>
            ))}
          </div>
        </div>
      </section>
      <Drawer
        title="结构化业务规则"
        open={showDrawer}
        onClose={() => setShowDrawer(false)}
        footer={<><button className="btn btn-default" onClick={() => setShowDrawer(false)}>取消</button><button className="btn btn-primary" onClick={() => setShowDrawer(false)}>纳入上下文</button></>}
      >
        <div className="field"><label>场景描述 *</label><textarea className="field-textarea" defaultValue="第三方系统通过任务结果接口获取结构化测试用例，要求状态校验与过期校验齐全。" /></div>
        <div className="field"><label>前置条件</label><textarea className="field-textarea" defaultValue="任务已完成，调用方具备对应应用访问权限。" /></div>
        <div className="field"><label>业务规则列表</label><textarea className="field-textarea" defaultValue={"1. 未完成任务不可获取结果。\n2. 结果过期需提示重新生成。\n3. 用例详情至少包含标题、步骤、预期和优先级。"} /></div>
      </Drawer>
      <Modal
        title="附件引用提交"
        open={showAttachment}
        onClose={() => setShowAttachment(false)}
        footer={<><button className="btn btn-default" onClick={() => setShowAttachment(false)}>取消</button><button className="btn btn-primary" onClick={() => setShowAttachment(false)}>引用成功</button></>}
      >
        <div className="overlay-grid">
          <div className="field"><label>附件名称 *</label><input className="field-input" placeholder="接口说明.md" /></div>
          <div className="field"><label>附件类型 *</label><select className="field-select"><option>需求文档</option><option>接口文档</option><option>原型说明</option></select></div>
          <div className="field"><label>附件地址 / 对象 ID *</label><input className="field-input" placeholder="https://files.example.com/open-api.md" /></div>
        </div>
      </Modal>
    </div>
  );
}
