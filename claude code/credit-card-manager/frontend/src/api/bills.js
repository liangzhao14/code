import request from '@/utils/request'

/** 获取账单列表（支持分页和筛选） */
export function getBills(params) {
  return request.get('/bills', { params })
}

/** 获取账单详情 */
export function getBill(id) {
  return request.get(`/bills/${id}`)
}

/** 新增账单 */
export function createBill(data) {
  return request.post('/bills', data)
}

/** 更新账单 */
export function updateBill(id, data) {
  return request.put(`/bills/${id}`, data)
}

/** 删除账单 */
export function deleteBill(id) {
  return request.delete(`/bills/${id}`)
}

/** 标记账单为已还款 */
export function markBillPaid(id) {
  return request.patch(`/bills/${id}/paid`)
}
