import request from '@/utils/request'

/** 获取信用卡列表 */
export function getCards(params) {
  return request.get('/cards', { params })
}

/** 获取单张信用卡详情 */
export function getCard(id) {
  return request.get(`/cards/${id}`)
}

/** 新增信用卡 */
export function createCard(data) {
  return request.post('/cards', data)
}

/** 更新信用卡 */
export function updateCard(id, data) {
  return request.put(`/cards/${id}`, data)
}

/** 删除信用卡 */
export function deleteCard(id) {
  return request.delete(`/cards/${id}`)
}
