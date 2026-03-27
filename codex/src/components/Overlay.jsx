export function Modal({ title, open, onClose, children, footer, widthClass = "" }) {
  return (
    <div className={`modal-mask${open ? " open" : ""}`}>
      <div className={`modal ${widthClass}`.trim()}>
        <div className="layer-header">
          <strong>{title}</strong>
          <button className="btn btn-link" onClick={onClose}>关闭</button>
        </div>
        <div className="layer-body">{children}</div>
        <div className="layer-footer">{footer}</div>
      </div>
    </div>
  );
}

export function Drawer({ title, open, onClose, children, footer }) {
  return (
    <div className={`drawer-mask${open ? " open" : ""}`}>
      <div className="drawer">
        <div className="layer-header">
          <strong>{title}</strong>
          <button className="btn btn-link" onClick={onClose}>关闭</button>
        </div>
        <div className="layer-body">{children}</div>
        <div className="layer-footer">{footer}</div>
      </div>
    </div>
  );
}
