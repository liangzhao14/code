import request from '@/utils/request'

/** 获取收入列表 */
export function getIncomes(params) {
  return request.get('/incomes', { params })
}

/** 获取收入详情 */
export function getIncome(id) {
  return request.get(`/incomes/${id}`)
}

/** 新增收入 */
export function createIncome(data) {
  return request.post('/incomes', data)
}

/** 更新收入 */
export function updateIncome(id, data) {
  return request.put(`/incomes/${id}`, data)
}

/** 删除收入 */
export function deleteIncome(id) {
  return request.delete(`/incomes/${id}`)
}
