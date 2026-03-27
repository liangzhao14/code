import request from '@/utils/request'

/** 获取分类列表 */
export function getCategories(params) {
  return request.get('/categories', { params })
}

/** 获取分类详情 */
export function getCategory(id) {
  return request.get(`/categories/${id}`)
}

/** 新增分类 */
export function createCategory(data) {
  return request.post('/categories', data)
}

/** 更新分类 */
export function updateCategory(id, data) {
  return request.put(`/categories/${id}`, data)
}

/** 删除分类 */
export function deleteCategory(id) {
  return request.delete(`/categories/${id}`)
}
