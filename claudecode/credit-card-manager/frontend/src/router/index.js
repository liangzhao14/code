import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/Login.vue'),
    meta: { requiresAuth: false }
  },
  {
    path: '/',
    name: 'Layout',
    component: () => import('@/views/Layout.vue'),
    meta: { requiresAuth: true },
    redirect: '/dashboard',
    children: [
      {
        path: 'dashboard',
        name: 'Dashboard',
        component: () => import('@/views/Dashboard.vue'),
        meta: { title: '仪表盘', requiresAuth: true }
      },
      {
        path: 'cards',
        name: 'CreditCards',
        component: () => import('@/views/CreditCards.vue'),
        meta: { title: '信用卡管理', requiresAuth: true }
      },
      {
        path: 'bills',
        name: 'Bills',
        component: () => import('@/views/Bills.vue'),
        meta: { title: '账单管理', requiresAuth: true }
      },
      {
        path: 'incomes',
        name: 'Incomes',
        component: () => import('@/views/Incomes.vue'),
        meta: { title: '收入管理', requiresAuth: true }
      },
      {
        path: 'expenses',
        name: 'Expenses',
        component: () => import('@/views/Expenses.vue'),
        meta: { title: '支出管理', requiresAuth: true }
      },
      {
        path: 'report',
        name: 'MonthlyReport',
        component: () => import('@/views/MonthlyReport.vue'),
        meta: { title: '月度报表', requiresAuth: true }
      }
    ]
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 路由守卫
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  if (to.meta.requiresAuth && !token) {
    next({ path: '/login', query: { redirect: to.fullPath } })
  } else if (to.path === '/login' && token) {
    next('/')
  } else {
    next()
  }
})

export default router
