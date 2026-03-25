import request from '@/utils/request'

export function getProfile() {
  return request.get('/user/profile')
}

export function updateAvatar(avatar) {
  return request.put('/user/avatar', { avatar })
}

export function uploadAvatar(file) {
  const formData = new FormData()
  formData.append('file', file)
  return request.post('/user/avatar/upload', formData)
}
