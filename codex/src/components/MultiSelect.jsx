export default function MultiSelect({ values, options, onToggle }) {
  return (
    <div className="multi-select">
      <div className="multi-select-trigger">
        {values.length === 0 ? (
          <span className="ms-placeholder">请选择（可多选）</span>
        ) : (
          values.map((value) => (
            <span className="ms-tag" key={value}>
              {value}
              <button className="btn btn-link ms-tag-close" onClick={() => onToggle(value)}>×</button>
            </span>
          ))
        )}
      </div>
      <div className="multi-select-dropdown" style={{ display: "flex", flexDirection: "column", gap: "8px", position: "static", boxShadow: "none", border: "none", padding: "8px 0 0" }}>
        {options.map((option) => (
          <label className="multi-select-option" key={option}>
            <input
              type="checkbox"
              checked={values.includes(option)}
              onChange={() => onToggle(option)}
            />
            {option}
          </label>
        ))}
      </div>
    </div>
  );
}
