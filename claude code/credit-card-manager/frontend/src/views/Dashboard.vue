<template>
  <div class="dashboard">
    <!-- 统计卡片 -->
    <el-row :gutter="20" class="stat-row">
      <el-col :xs="24" :sm="12" :lg="6">
        <div class="stat-card" style="--accent: #67c23a">
          <div class="stat-icon-wrap">
            <el-icon class="stat-icon"><TrendCharts /></el-icon>
          </div>
          <div class="stat-content">
            <p class="stat-label">本月收入</p>
            <p class="stat-value">¥{{ formatNumber(overview.income) }}</p>
          </div>
        </div>
      </el-col>
      <el-col :xs="24" :sm="12" :lg="6">
        <div class="stat-card" style="--accent: #f56c6c">
          <div class="stat-icon-wrap">
            <el-icon class="stat-icon"><ShoppingCart /></el-icon>
          </div>
          <div class="stat-content">
            <p class="stat-label">本月支出</p>
            <p class="stat-value">¥{{ formatNumber(overview.expense) }}</p>
          </div>
        </div>
      </el-col>
      <el-col :xs="24" :sm="12" :lg="6">
        <div class="stat-card" style="--accent: #409eff">
          <div class="stat-icon-wrap">
            <el-icon class="stat-icon"><DataAnalysis /></el-icon>
          </div>
          <div class="stat-content">
            <p class="stat-label">本月结余</p>
            <p class="stat-value" :class="overview.balance >= 0 ? 'positive' : 'negative'">
              {{ overview.balance >= 0 ? '+' : '' }}¥{{ formatNumber(Math.abs(overview.balance)) }}
            </p>
          </div>
        </div>
      </el-col>
      <el-col :xs="24" :sm="12" :lg="6">
        <div class="stat-card" style="--accent: #e6a23c">
          <div class="stat-icon-wrap">
            <el-icon class="stat-icon"><Document /></el-icon>
          </div>
          <div class="stat-content">
            <p class="stat-label">环比支出变化</p>
            <p class="stat-value" :class="comparison.expenseDiff > 0 ? 'negative' : 'positive'">
              {{ comparison.expenseDiff > 0 ? '+' : '' }}¥{{ formatNumber(Math.abs(comparison.expenseDiff)) }}
            </p>
          </div>
        </div>
      </el-col>
    </el-row>

    <!-- 图表区域 -->
    <el-row :gutter="20" class="chart-row">
      <!-- 收支趋势折线图 -->
      <el-col :xs="24" :lg="14">
        <div class="chart-card">
          <div class="card-title">
            <span>近6个月收支趋势</span>
            <el-tag type="info" size="small">月度</el-tag>
          </div>
          <div ref="trendChartRef" class="chart-container"></div>
        </div>
      </el-col>

      <!-- 本月 vs 上月对比 -->
      <el-col :xs="24" :lg="10">
        <div class="chart-card">
          <div class="card-title">
            <span>本月 vs 上月</span>
          </div>
          <div ref="compareChartRef" class="chart-container"></div>
        </div>
      </el-col>
    </el-row>

    <!-- 近期待还信用卡 -->
    <div class="table-card">
      <div class="card-title">
        <span>近7天待还信用卡</span>
        <el-button size="small" type="primary" text @click="$router.push('/bills')">
          查看全部账单
        </el-button>
      </div>
      <el-table :data="upcomingPayments" stripe style="width: 100%">
        <el-table-column prop="cardName" label="信用卡" width="160" />
        <el-table-column prop="bankName" label="银行" width="120" />
        <el-table-column prop="cardLastFour" label="卡尾号" width="100">
          <template #default="{ row }">
            <span>**** {{ row.cardLastFour }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="dueDate" label="还款日" width="130" />
        <el-table-column prop="daysUntilDue" label="剩余天数" width="120">
          <template #default="{ row }">
            <el-tag :type="row.daysUntilDue <= 2 ? 'danger' : 'warning'" size="small">
              {{ row.daysUntilDue === 0 ? '今天' : row.daysUntilDue + '天后' }}
            </el-tag>
          </template>
        </el-table-column>
      </el-table>
      <el-empty v-if="upcomingPayments.length === 0" description="近7天内无需还款" :image-size="60" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import * as echarts from 'echarts'
import { getDashboardData, getTrend } from '@/api/summary'

const trendChartRef = ref(null)
const compareChartRef = ref(null)
let trendChart = null
let compareChart = null

const overview = ref({ income: 0, expense: 0, balance: 0 })
const comparison = ref({ currentIncome: 0, lastIncome: 0, currentExpense: 0, lastExpense: 0, incomeDiff: 0, expenseDiff: 0 })
const upcomingPayments = ref([])

function formatNumber(val) {
  if (val === undefined || val === null) return '0.00'
  return Number(val).toLocaleString('zh-CN', { minimumFractionDigits: 2, maximumFractionDigits: 2 })
}

function initTrendChart(data) {
  if (!trendChartRef.value) return
  trendChart = echarts.init(trendChartRef.value)
  trendChart.setOption({
    tooltip: { trigger: 'axis', axisPointer: { type: 'cross' } },
    legend: { data: ['收入', '支出', '结余'], bottom: 0 },
    grid: { top: 16, left: 16, right: 16, bottom: 40, containLabel: true },
    xAxis: { type: 'category', data: data.months, boundaryGap: false },
    yAxis: { type: 'value', axisLabel: { formatter: '¥{value}' } },
    series: [
      {
        name: '收入', type: 'line', data: data.incomes, smooth: true,
        lineStyle: { color: '#67c23a', width: 2 }, itemStyle: { color: '#67c23a' },
        areaStyle: { color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1, colorStops: [{ offset: 0, color: 'rgba(103,194,58,0.3)' }, { offset: 1, color: 'rgba(103,194,58,0)' }] } }
      },
      {
        name: '支出', type: 'line', data: data.expenses, smooth: true,
        lineStyle: { color: '#f56c6c', width: 2 }, itemStyle: { color: '#f56c6c' },
        areaStyle: { color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1, colorStops: [{ offset: 0, color: 'rgba(245,108,108,0.3)' }, { offset: 1, color: 'rgba(245,108,108,0)' }] } }
      },
      {
        name: '结余', type: 'line', data: data.balances, smooth: true,
        lineStyle: { color: '#409eff', width: 2, type: 'dashed' }, itemStyle: { color: '#409eff' }
      }
    ]
  })
}

function initCompareChart(comp) {
  if (!compareChartRef.value) return
  compareChart = echarts.init(compareChartRef.value)
  compareChart.setOption({
    tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
    legend: { data: ['上月', '本月'], bottom: 0 },
    grid: { top: 16, left: 16, right: 16, bottom: 40, containLabel: true },
    xAxis: { type: 'category', data: ['收入', '支出'] },
    yAxis: { type: 'value', axisLabel: { formatter: '¥{value}' } },
    series: [
      { name: '上月', type: 'bar', data: [comp.lastIncome, comp.lastExpense], itemStyle: { color: '#909399', borderRadius: [4, 4, 0, 0] } },
      { name: '本月', type: 'bar', data: [comp.currentIncome, comp.currentExpense], itemStyle: { color: '#409eff', borderRadius: [4, 4, 0, 0] } }
    ]
  })
}

function handleResize() {
  trendChart?.resize()
  compareChart?.resize()
}

onMounted(async () => {
  // 加载仪表盘数据
  try {
    const res = await getDashboardData()
    if (res.data) {
      overview.value = res.data.monthOverview || overview.value
      comparison.value = res.data.comparison || comparison.value
      upcomingPayments.value = res.data.upcomingPayments || []
    }
  } catch { /* 使用默认值 */ }

  // 初始化对比图
  initCompareChart(comparison.value)

  // 加载趋势数据
  try {
    const res = await getTrend()
    if (res.data) {
      initTrendChart(res.data)
    }
  } catch {
    initTrendChart({ months: [], incomes: [], expenses: [], balances: [] })
  }

  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  trendChart?.dispose()
  compareChart?.dispose()
})
</script>

<style scoped>
.dashboard {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.stat-card {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 20px 24px;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 1px 6px rgba(0, 0, 0, 0.06);
  border-left: 4px solid var(--accent);
  transition: box-shadow 0.2s;
}

.stat-card:hover {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.stat-icon-wrap {
  width: 52px;
  height: 52px;
  border-radius: 12px;
  background-color: color-mix(in srgb, var(--accent) 15%, transparent);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.stat-icon {
  font-size: 24px;
  color: var(--accent);
}

.stat-label {
  font-size: 13px;
  color: #909399;
  margin-bottom: 4px;
}

.stat-value {
  font-size: 22px;
  font-weight: 700;
  color: #1a1f2e;
}

.stat-value.positive { color: #67c23a; }
.stat-value.negative { color: #f56c6c; }

.chart-card,
.table-card {
  background: #ffffff;
  border-radius: 12px;
  padding: 20px 24px;
  box-shadow: 0 1px 6px rgba(0, 0, 0, 0.06);
}

.card-title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 15px;
  font-weight: 600;
  color: #1a1f2e;
  margin-bottom: 16px;
  gap: 8px;
}

.chart-container {
  height: 280px;
  width: 100%;
}

@media (max-width: 768px) {
  .stat-card { margin-bottom: 16px; }
  .chart-card { margin-bottom: 16px; }
}
</style>
