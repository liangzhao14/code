<template>
  <el-container class="layout-container">
    <!-- 侧边栏 -->
    <el-aside :width="isCollapsed ? '64px' : '220px'" class="sidebar" :class="{ collapsed: isCollapsed }">
      <!-- Logo 区域 -->
      <div class="sidebar-logo">
        <el-icon class="logo-icon"><CreditCard /></el-icon>
        <span v-show="!isCollapsed" class="logo-text">信用卡管理</span>
      </div>

      <!-- 导航菜单 -->
      <el-menu
        :default-active="activeMenu"
        router
        :collapse="isCollapsed"
        class="sidebar-menu"
      >
        <el-menu-item index="/dashboard">
          <el-icon><Odometer /></el-icon>
          <template #title>仪表盘</template>
        </el-menu-item>
        <el-menu-item index="/cards">
          <el-icon><CreditCard /></el-icon>
          <template #title>信用卡管理</template>
        </el-menu-item>
        <el-menu-item index="/bills">
          <el-icon><Document /></el-icon>
          <template #title>账单管理</template>
        </el-menu-item>
        <el-menu-item index="/incomes">
          <el-icon><TrendCharts /></el-icon>
          <template #title>收入管理</template>
        </el-menu-item>
        <el-menu-item index="/expenses">
          <el-icon><ShoppingCart /></el-icon>
          <template #title>支出管理</template>
        </el-menu-item>
        <el-menu-item index="/report">
          <el-icon><DataAnalysis /></el-icon>
          <template #title>月度报表</template>
        </el-menu-item>
      </el-menu>

      <!-- 折叠按钮 -->
      <div class="collapse-btn" @click="isCollapsed = !isCollapsed">
        <el-icon>
          <Fold v-if="!isCollapsed" />
          <Expand v-else />
        </el-icon>
      </div>
    </el-aside>

    <!-- 右侧主区域 -->
    <el-container class="main-container">
      <!-- 顶部栏 -->
      <el-header class="header">
        <div class="header-left">
          <span class="page-title">{{ currentTitle }}</span>
        </div>
        <div class="header-right">
          <el-popover
            placement="bottom-end"
            :width="360"
            trigger="click"
            @show="loadNotifications"
          >
            <template #reference>
              <el-badge :value="unreadCount" :hidden="unreadCount === 0" :max="99">
                <el-icon class="header-icon"><Bell /></el-icon>
              </el-badge>
            </template>
            <div class="notification-panel">
              <div class="notification-header">
                <span class="notification-title">通知中心</span>
                <span class="notification-count" v-if="notifications.length">{{ notifications.length }} 条通知</span>
              </div>
              <div v-if="notificationLoading" class="notification-loading">
                <el-icon class="is-loading"><Loading /></el-icon>
                <span>加载中...</span>
              </div>
              <div v-else-if="notifications.length === 0" class="notification-empty">
                <el-icon :size="32" color="#c0c4cc"><BellFilled /></el-icon>
                <span>暂无通知</span>
              </div>
              <div v-else class="notification-list">
                <div
                  v-for="(item, index) in notifications"
                  :key="index"
                  class="notification-item"
                  :class="'notification-' + item.level"
                >
                  <div class="notification-item-icon">
                    <el-icon v-if="item.type === 'repayment'" :color="levelColor(item.level)"><Timer /></el-icon>
                    <el-icon v-else-if="item.type === 'overdue'" color="#f56c6c"><WarningFilled /></el-icon>
                    <el-icon v-else color="#909399"><InfoFilled /></el-icon>
                  </div>
                  <div class="notification-item-content">
                    <div class="notification-item-title">{{ item.title }}</div>
                    <div v-if="item.type === 'repayment'" class="notification-item-desc">
                      {{ item.bankName }} ({{ item.cardLastFour }}) · 账单 ¥{{ item.billAmount }}
                    </div>
                    <div v-else-if="item.type === 'overdue'" class="notification-item-desc">
                      {{ item.bankName }} · 账单 ¥{{ item.billAmount }}
                    </div>
                    <div v-else-if="item.type === 'system'" class="notification-item-desc">
                      收入 ¥{{ item.income }} · 支出 ¥{{ item.expense }} · 结余 ¥{{ item.balance }}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </el-popover>
          <el-dropdown @command="handleUserCommand">
            <div class="user-info">
              <el-avatar :size="32" :src="avatarUrl" fit="cover" class="user-avatar">
                {{ username.charAt(0).toUpperCase() }}
              </el-avatar>
              <span class="username">{{ username }}</span>
              <el-icon class="arrow-icon"><ArrowDown /></el-icon>
            </div>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item command="changeAvatar">
                  <el-icon><Picture /></el-icon>
                  更换头像
                </el-dropdown-item>
                <el-dropdown-item command="logout" divided>
                  <el-icon><SwitchButton /></el-icon>
                  退出登录
                </el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </el-header>

      <!-- 内容区域 -->
      <el-main class="main-content">
        <router-view v-slot="{ Component }">
          <transition name="fade" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </el-main>
    </el-container>

    <!-- 头像选择弹窗 -->
    <el-dialog
      v-model="avatarDialogVisible"
      title="更换头像"
      width="480px"
      class="avatar-dialog"
      :close-on-click-modal="false"
    >
      <div class="avatar-dialog-body">
        <!-- 当前头像预览 -->
        <div class="avatar-preview-section">
          <el-avatar :size="80" :src="previewAvatarUrl" fit="cover" class="avatar-preview">
            {{ username.charAt(0).toUpperCase() }}
          </el-avatar>
          <span class="avatar-preview-label">当前头像</span>
        </div>

        <!-- 预设头像选择 -->
        <div class="avatar-section-title">选择预设头像</div>
        <div class="preset-avatar-grid">
          <div
            v-for="i in 6"
            :key="i"
            class="preset-avatar-item"
            :class="{ active: selectedAvatar === 'preset:' + i }"
            @click="selectPreset(i)"
          >
            <el-avatar :size="56" :src="'/avatars/preset-' + i + '.svg'" fit="cover" />
          </div>
        </div>

        <!-- 自定义上传 -->
        <div class="avatar-section-title">自定义上传</div>
        <div class="upload-section">
          <el-upload
            :auto-upload="false"
            :show-file-list="false"
            accept="image/jpeg,image/png,image/gif,image/webp"
            :on-change="handleFileChange"
          >
            <el-button type="primary" plain>
              <el-icon><Upload /></el-icon>
              选择图片
            </el-button>
          </el-upload>
          <span class="upload-tip">支持 JPG/PNG/GIF/WebP，不超过 2MB</span>
        </div>
      </div>
      <template #footer>
        <el-button @click="avatarDialogVisible = false">取消</el-button>
        <el-button type="primary" :loading="avatarSaving" @click="saveAvatar">确认</el-button>
      </template>
    </el-dialog>
  </el-container>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { ElMessageBox, ElMessage } from 'element-plus'
import { useUserStore } from '@/stores/user'
import { getNotifications } from '@/api/notifications'
import { updateAvatar as apiUpdateAvatar, uploadAvatar as apiUploadAvatar } from '@/api/user'

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()

const isCollapsed = ref(false)

// 头像相关
function resolveAvatarUrl(avatar) {
  if (!avatar) return ''
  if (avatar.startsWith('preset:')) {
    return '/avatars/preset-' + avatar.split(':')[1] + '.svg'
  }
  return '/api/avatars/uploads/' + avatar
}

const avatarUrl = computed(() => resolveAvatarUrl(userStore.avatar))

const avatarDialogVisible = ref(false)
const selectedAvatar = ref('')
const customFile = ref(null)
const avatarSaving = ref(false)

const previewAvatarUrl = computed(() => {
  if (customFile.value) {
    return URL.createObjectURL(customFile.value)
  }
  return resolveAvatarUrl(selectedAvatar.value)
})

function selectPreset(i) {
  selectedAvatar.value = 'preset:' + i
  customFile.value = null
}

function handleFileChange(uploadFile) {
  const file = uploadFile.raw
  if (file.size > 2 * 1024 * 1024) {
    ElMessage.warning('文件大小不能超过 2MB')
    return
  }
  customFile.value = file
  selectedAvatar.value = ''
}

async function saveAvatar() {
  avatarSaving.value = true
  try {
    if (customFile.value) {
      const res = await apiUploadAvatar(customFile.value)
      userStore.updateAvatar(res.data)
      ElMessage.success('头像上传成功')
    } else if (selectedAvatar.value) {
      await apiUpdateAvatar(selectedAvatar.value)
      userStore.updateAvatar(selectedAvatar.value)
      ElMessage.success('头像更新成功')
    } else {
      ElMessage.info('请选择一个头像')
      avatarSaving.value = false
      return
    }
    avatarDialogVisible.value = false
  } catch {
    // 错误已由拦截器处理
  } finally {
    avatarSaving.value = false
    customFile.value = null
  }
}

// 通知相关
const notifications = ref([])
const unreadCount = ref(0)
const notificationLoading = ref(false)

function levelColor(level) {
  const map = { danger: '#f56c6c', warning: '#e6a23c', info: '#909399' }
  return map[level] || '#909399'
}

async function loadNotifications() {
  notificationLoading.value = true
  try {
    const res = await getNotifications()
    notifications.value = res.data.notifications || []
    unreadCount.value = res.data.unreadCount || 0
  } catch {
    notifications.value = []
    unreadCount.value = 0
  } finally {
    notificationLoading.value = false
  }
}

// 进入页面时加载一次通知角标数量，之后每60秒刷新
let pollTimer = null
onMounted(() => {
  loadNotifications()
  pollTimer = setInterval(loadNotifications, 60000)
})
onUnmounted(() => {
  if (pollTimer) clearInterval(pollTimer)
})

const activeMenu = computed(() => route.path)
const username = computed(() => userStore.username || '用户')

const titleMap = {
  '/dashboard': '仪表盘',
  '/cards': '信用卡管理',
  '/bills': '账单管理',
  '/incomes': '收入管理',
  '/expenses': '支出管理',
  '/report': '月度报表'
}
const currentTitle = computed(() => titleMap[route.path] || '信用卡还款与收支管理')

async function handleUserCommand(command) {
  if (command === 'changeAvatar') {
    selectedAvatar.value = userStore.avatar || 'preset:1'
    customFile.value = null
    avatarDialogVisible.value = true
    return
  }
  if (command === 'logout') {
    try {
      await ElMessageBox.confirm('确定要退出登录吗？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      })
      userStore.logout()
      ElMessage.success('已退出登录')
      router.push('/login')
    } catch {
      // 用户取消
    }
  }
}
</script>

<style scoped>
/* ===== 全局色彩变量 ===== */
:root {
  --sidebar-bg: #0f1423;
  --sidebar-bg-light: #161b2e;
  --sidebar-border: rgba(255, 255, 255, 0.06);
  --sidebar-text: #8892a8;
  --sidebar-text-hover: #c8cfe0;
  --sidebar-text-active: #ffffff;
  --sidebar-icon: #6b7590;
  --sidebar-icon-hover: #a0aec0;
  --sidebar-icon-active: #ffffff;
  --primary: #3b82f6;
  --primary-light: rgba(59, 130, 246, 0.12);
  --primary-glow: rgba(59, 130, 246, 0.35);
  --header-bg: #ffffff;
  --content-bg: #f0f2f5;
  --text-primary: #1a1f2e;
  --text-secondary: #606266;
  --text-muted: #909399;
}

.layout-container {
  height: 100vh;
  overflow: hidden;
}

/* ===== 侧边栏 ===== */
.sidebar {
  background: linear-gradient(180deg, var(--sidebar-bg) 0%, var(--sidebar-bg-light) 100%);
  display: flex;
  flex-direction: column;
  transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  overflow: hidden;
  box-shadow: 2px 0 12px rgba(0, 0, 0, 0.4);
  z-index: 20;
}

/* Logo */
.sidebar-logo {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 22px 20px;
  border-bottom: 1px solid var(--sidebar-border);
  min-height: 68px;
  overflow: hidden;
  transition: padding 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.sidebar.collapsed .sidebar-logo {
  justify-content: center;
  padding: 22px 10px;
}

.logo-icon {
  font-size: 20px;
  color: var(--primary);
  flex-shrink: 0;
  filter: drop-shadow(0 0 6px var(--primary-glow));
  width: 20px;
  text-align: center;
}

.logo-text {
  font-size: 16px;
  font-weight: 700;
  color: var(--sidebar-text-active);
  white-space: nowrap;
  letter-spacing: 1px;
}

/* 菜单整体 */
.sidebar-menu {
  flex: 1;
  border-right: none !important;
  overflow-y: auto;
  overflow-x: hidden;
  padding: 8px 0;
  background-color: transparent !important;
}

/* 覆盖 el-menu 默认背景 */
.sidebar-menu:deep(.el-menu) {
  background-color: transparent !important;
}

/* 菜单项 — 展开态 */
.sidebar-menu:deep(.el-menu-item) {
  height: 48px;
  line-height: 48px;
  border-radius: 10px;
  margin: 3px 10px;
  padding: 0 16px !important;
  color: var(--sidebar-text) !important;
  background-color: transparent !important;
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 0.3px;
}

.sidebar-menu:deep(.el-menu-item .el-icon) {
  font-size: 20px;
  color: var(--sidebar-icon);
  transition: all 0.25s ease;
  margin-right: 10px;
  width: 20px;
  text-align: center;
}

/* 菜单项 — 折叠态：图标居中，与顶部 Logo 对齐 */
.sidebar.collapsed :deep(.el-menu-item) {
  padding: 0 !important;
  margin: 3px 10px;
  border-radius: 10px;
}

.sidebar.collapsed :deep(.el-menu-item .el-icon) {
  margin-right: 0;
}

.sidebar.collapsed :deep(.el-menu-tooltip__trigger) {
  padding: 0 !important;
  display: flex !important;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
}

/* 悬浮态 */
.sidebar-menu:deep(.el-menu-item:hover) {
  background-color: var(--primary-light) !important;
  color: var(--sidebar-text-hover) !important;
}

.sidebar-menu:deep(.el-menu-item:hover .el-icon) {
  color: var(--sidebar-icon-hover) !important;
  transform: scale(1.08);
}

/* 选中态 */
.sidebar-menu:deep(.el-menu-item.is-active) {
  background: linear-gradient(135deg, var(--primary), #2563eb) !important;
  color: var(--sidebar-text-active) !important;
  box-shadow: 0 4px 14px var(--primary-glow);
  font-weight: 600;
}

.sidebar-menu:deep(.el-menu-item.is-active .el-icon) {
  color: var(--sidebar-icon-active) !important;
  filter: drop-shadow(0 0 4px rgba(255, 255, 255, 0.4));
}

/* 选中态左侧指示条 */
.sidebar-menu:deep(.el-menu-item.is-active::before) {
  content: '';
  position: absolute;
  left: -10px;
  top: 50%;
  transform: translateY(-50%);
  width: 4px;
  height: 24px;
  background: var(--sidebar-text-active);
  border-radius: 0 4px 4px 0;
  opacity: 0.9;
}

/* 折叠态选中 — 隐藏左侧条 */
.sidebar.collapsed :deep(.el-menu-item.is-active::before) {
  display: none;
}

/* 菜单滚动条美化 */
.sidebar-menu::-webkit-scrollbar {
  width: 3px;
}

.sidebar-menu::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 3px;
}

.sidebar-menu::-webkit-scrollbar-track {
  background: transparent;
}

/* 折叠按钮 */
.collapse-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 48px;
  cursor: pointer;
  color: var(--sidebar-icon);
  border-top: 1px solid var(--sidebar-border);
  font-size: 18px;
  transition: all 0.25s ease;
}

.collapse-btn:hover {
  color: var(--sidebar-text-active);
  background-color: var(--primary-light);
}

/* ===== 顶部栏 ===== */
.main-container {
  background-color: var(--content-bg);
}

.header {
  background-color: var(--header-bg);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08);
  height: 60px !important;
  z-index: 10;
}

.header-left .page-title {
  font-size: 18px;
  font-weight: 600;
  color: var(--text-primary);
}

.header-right {
  display: flex;
  align-items: center;
  gap: 20px;
}

.header-icon {
  font-size: 20px;
  color: var(--text-secondary);
  cursor: pointer;
  transition: color 0.2s;
}

.header-icon:hover {
  color: var(--primary);
}

.user-info {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  padding: 4px 8px;
  border-radius: 8px;
  transition: background-color 0.2s;
}

.user-info:hover {
  background-color: #f5f7fa;
}

.user-avatar {
  background: linear-gradient(135deg, var(--primary), #2563eb);
  font-size: 14px;
  font-weight: 600;
  flex-shrink: 0;
  overflow: hidden;
}

.user-avatar :deep(img) {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.username {
  font-size: 14px;
  color: var(--text-primary);
  font-weight: 500;
}

.arrow-icon {
  font-size: 12px;
  color: var(--text-muted);
}

/* ===== 内容区 ===== */
.main-content {
  padding: 24px;
  overflow-y: auto;
  background-color: var(--content-bg);
}

/* 路由过渡动画 */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* 通知面板 */
.notification-panel {
  margin: -12px;
}

.notification-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  border-bottom: 1px solid #ebeef5;
}

.notification-title {
  font-size: 15px;
  font-weight: 600;
  color: #303133;
}

.notification-count {
  font-size: 12px;
  color: #909399;
}

.notification-loading,
.notification-empty {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 32px 0;
  color: #909399;
  font-size: 14px;
}

.notification-list {
  max-height: 360px;
  overflow-y: auto;
}

.notification-item {
  display: flex;
  gap: 10px;
  padding: 12px 16px;
  border-bottom: 1px solid #f2f3f5;
  transition: background-color 0.2s;
}

.notification-item:last-child {
  border-bottom: none;
}

.notification-item:hover {
  background-color: #f5f7fa;
}

.notification-item-icon {
  flex-shrink: 0;
  margin-top: 2px;
  font-size: 18px;
}

.notification-item-content {
  flex: 1;
  min-width: 0;
}

.notification-item-title {
  font-size: 14px;
  font-weight: 500;
  color: #303133;
  margin-bottom: 4px;
}

.notification-danger .notification-item-title {
  color: #f56c6c;
}

.notification-warning .notification-item-title {
  color: #e6a23c;
}

.notification-item-desc {
  font-size: 12px;
  color: #909399;
  line-height: 1.5;
}

/* 头像弹窗 */
.avatar-dialog-body {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.avatar-preview-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.avatar-preview {
  border: 3px solid var(--primary);
  background: linear-gradient(135deg, var(--primary), #2563eb);
  overflow: hidden;
}

.avatar-preview :deep(img) {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.avatar-preview-label {
  font-size: 13px;
  color: var(--text-muted);
}

.avatar-section-title {
  width: 100%;
  font-size: 14px;
  font-weight: 600;
  color: var(--text-primary);
  padding-bottom: 4px;
  border-bottom: 1px solid #ebeef5;
}

.preset-avatar-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 12px;
  width: 100%;
}

.preset-avatar-item {
  display: flex;
  justify-content: center;
  cursor: pointer;
  padding: 6px;
  border-radius: 12px;
  border: 2px solid transparent;
  transition: all 0.2s;
}

.preset-avatar-item :deep(.el-avatar) {
  overflow: hidden;
}

.preset-avatar-item :deep(img) {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.preset-avatar-item:hover {
  border-color: #c6e2ff;
  background-color: #ecf5ff;
}

.preset-avatar-item.active {
  border-color: var(--primary);
  background-color: #ecf5ff;
  box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2);
}

.upload-section {
  display: flex;
  align-items: center;
  gap: 12px;
  width: 100%;
}

.upload-tip {
  font-size: 12px;
  color: var(--text-muted);
}
</style>
