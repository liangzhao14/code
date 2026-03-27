import { NavLink, Outlet, useLocation } from "react-router-dom";
import { useMemo, useState } from "react";
import { navGroups, notifications } from "../data/mockData";

function breadcrumbItems(pathname) {
  if (pathname.startsWith("/apps/")) return ["首页", "开放接入", "应用详情"];
  if (pathname === "/apps") return ["首页", "开放接入", "接入管理"];
  if (pathname === "/generate") return ["首页", "生成服务", "生成工作台"];
  if (pathname.startsWith("/tasks/")) return ["首页", "任务管理", "任务详情"];
  if (pathname.startsWith("/results/CASE")) return ["首页", "结果中心", "用例详情"];
  if (pathname === "/results") return ["首页", "结果中心", "结果列表"];
  return ["首页", "监控工作台"];
}

export default function AppLayout() {
  const location = useLocation();
  const crumbs = useMemo(() => breadcrumbItems(location.pathname), [location.pathname]);
  const [showNotify, setShowNotify] = useState(false);
  const [showAvatar, setShowAvatar] = useState(false);

  return (
    <div className="page-shell">
      <div className="app-shell">
        <aside className="sidebar">
          <div className="brand"><span className="logo-icon">TC</span><span className="logo-text">CaseFlow API</span></div>
          {navGroups.map((group) => (
            <div className="nav-group" key={group.title}>
              <div className="nav-group-title">{group.title}</div>
              {group.items.map((item) => (
                <div className={item.indent ? "nav-submenu" : ""} key={item.to}>
                  <NavLink className={({ isActive }) => `nav-link${isActive ? " active" : ""}`} to={item.to}>
                    <span className="nav-icon">{item.icon}</span>
                    {item.label}
                  </NavLink>
                </div>
              ))}
            </div>
          ))}
        </aside>
        <main className="content-shell">
          <div className="topbar">
            <div className="topbar-left">
              <div className="breadcrumb">
                {crumbs.map((item, index) => (
                  <span key={item}>
                    {index > 0 ? <span> / </span> : null}
                    {index === crumbs.length - 1 ? <span className="current">{item}</span> : <span>{item}</span>}
                  </span>
                ))}
              </div>
            </div>
            <div className="topbar-right">
              <input className="topbar-search" placeholder="搜索应用、任务或结果" />
              <button
                className="topbar-icon-btn"
                onClick={() => {
                  setShowAvatar(false);
                  setShowNotify((value) => !value);
                }}
              >
                🔔
                <span className="badge-dot" />
                <div className={`topbar-dropdown topbar-notify-panel${showNotify ? " open" : ""}`}>
                  <div className="topbar-notify-header"><span>消息通知</span><span>全部已读</span></div>
                  {notifications.map((item) => (
                    <div className="topbar-notify-item" key={item.text}>
                      <span className={`topbar-notify-dot${item.unread ? "" : " read"}`} />
                      <div className="topbar-notify-content">
                        <div className="topbar-notify-text">{item.text}</div>
                        <div className="topbar-notify-time">{item.time}</div>
                      </div>
                    </div>
                  ))}
                </div>
              </button>
              <button
                className="topbar-avatar"
                onClick={() => {
                  setShowNotify(false);
                  setShowAvatar((value) => !value);
                }}
              >
                张
                <div className={`topbar-dropdown topbar-avatar-menu${showAvatar ? " open" : ""}`}>
                  <div className="topbar-avatar-menu-item">个人中心</div>
                  <div className="topbar-avatar-menu-item">账户设置</div>
                  <div className="topbar-avatar-menu-divider" />
                  <div className="topbar-avatar-menu-item">退出登录</div>
                </div>
              </button>
            </div>
          </div>
          <Outlet />
        </main>
      </div>
    </div>
  );
}
