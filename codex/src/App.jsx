import { Navigate, Route, Routes } from "react-router-dom";
import AppLayout from "./layouts/AppLayout";
import DashboardPage from "./pages/DashboardPage";
import AppAccessPage from "./pages/AppAccessPage";
import AppDetailPage from "./pages/AppDetailPage";
import GenerateRequestPage from "./pages/GenerateRequestPage";
import TaskDetailPage from "./pages/TaskDetailPage";
import ResultCenterPage from "./pages/ResultCenterPage";
import CaseDetailPage from "./pages/CaseDetailPage";

export default function App() {
  return (
    <Routes>
      <Route element={<AppLayout />}>
        <Route index element={<Navigate to="/dashboard" replace />} />
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/apps" element={<AppAccessPage />} />
        <Route path="/apps/:appId" element={<AppDetailPage />} />
        <Route path="/generate" element={<GenerateRequestPage />} />
        <Route path="/tasks/:taskId" element={<TaskDetailPage />} />
        <Route path="/results" element={<ResultCenterPage />} />
        <Route path="/results/:caseId" element={<CaseDetailPage />} />
      </Route>
    </Routes>
  );
}
