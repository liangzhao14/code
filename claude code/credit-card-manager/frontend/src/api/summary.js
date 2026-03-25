import request from '@/utils/request'

/** 获取仪表盘概览数据 */
export function getDashboardData() {
  return request.get('/dashboard')
}

/** 获取月度汇总数据 */
export function getMonthlySummary(params) {
  return request.get('/summary/monthly', { params })
}

/** 获取收支趋势（近6个月） */
export function getTrend() {
  return request.get('/summary/trend')
}
