import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
  const token = ref(localStorage.getItem('token') || '')
  const userInfo = ref(JSON.parse(localStorage.getItem('userInfo') || 'null'))

  const isLoggedIn = computed(() => !!token.value)
  const username = computed(() => userInfo.value?.username || '')
  const avatar = computed(() => userInfo.value?.avatar || 'preset:1')

  function setToken(newToken) {
    token.value = newToken
    localStorage.setItem('token', newToken)
  }

  function setUserInfo(info) {
    userInfo.value = info
    localStorage.setItem('userInfo', JSON.stringify(info))
  }

  function login(newToken, info) {
    setToken(newToken)
    if (info) setUserInfo(info)
  }

  function logout() {
    token.value = ''
    userInfo.value = null
    localStorage.removeItem('token')
    localStorage.removeItem('userInfo')
  }

  function updateAvatar(newAvatar) {
    if (userInfo.value) {
      userInfo.value = { ...userInfo.value, avatar: newAvatar }
      localStorage.setItem('userInfo', JSON.stringify(userInfo.value))
    }
  }

  return {
    token,
    userInfo,
    isLoggedIn,
    username,
    avatar,
    setToken,
    setUserInfo,
    login,
    logout,
    updateAvatar
  }
})
