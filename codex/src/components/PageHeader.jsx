export default function PageHeader({ title, subtitle, actions }) {
  return (
    <section className="page-header">
      <div>
        <h1 className="page-title">{title}</h1>
        <p className="page-subtitle">{subtitle}</p>
      </div>
      <div className="toolbar-right">{actions}</div>
    </section>
  );
}
