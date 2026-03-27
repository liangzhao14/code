export default function DetailGrid({ items }) {
  return (
    <div className="desc-grid">
      {items.map((item) => (
        <div className="desc-item" key={`${item.label}-${item.value}`}>
          <div className="desc-label">{item.label}</div>
          <div className="desc-value">
            {item.tone ? <span className={`tag tag-${item.tone}`}>{item.value}</span> : item.value}
          </div>
        </div>
      ))}
    </div>
  );
}
