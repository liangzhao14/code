<template>
  <div class="page-wrap">
    <!-- 月份选择 -->
    <div class="toolbar">
      <div class="filter-group">
        <span class="filter-label">报表月份：</span>
        <el-date-picker
          v-model="selectedMonth"
          type="month"
          placeholder="选择月份"
          format="YYYY年MM月"
          value-format="YYYY-MM"
          :disabled-date="disableFuture"
          style="width:160px"
          @change="loadReport"
        />
      </div>
      <el-button :icon="Refresh" @click="loadReport">刷新</el-button>
    </div>

    <!-- 本月总览 -->
    <el-row :gutter="20">
      <el-col :xs="24" :sm="6">
        <div class="overview-card income">
          <p class="ov-label">总收入</p>
          <p class="ov-value">¥{{ formatNum(report.totalIncome) }}</p>
        </div>
      </el-col>
      <el-col :xs="24" :sm="6">
        <div class="overview-card expense">
          <p class="ov-label">总支出</p>
          <p class="ov-value">¥{{ formatNum(report.totalExpense) }}</p>
        </div>
      </el-col>
      <el-col :xs="24" :sm="6">
        <div class="overview-card" :class="report.balance >= 0 ? 'positive' : 'negative'">
          <p class="ov-label">结余</p>
          <p class="ov-value">{{ report.balance >= 0 ? '+' : '' }}¥{{ formatNum(Math.abs(report.balance || 0)) }}</p>
        </div>
      </el-col>
      <el-col :xs="24" :sm="6">
        <div class="overview-card payment">
          <p class="ov-label">信用卡还款</p>
          <p class="ov-value">¥{{ formatNum(report.cardPaymentTotal) }}</p>
        </div>
      </el-col>
    </el-row>

    <!-- 图表区域 -->
    <el-row :gutter="20">
      <!-- 近6月趋势 -->
      <el-col :xs="24" :lg="14">
        <div class="chart-card">
          <div class="card-title">近6个月趋势</div>
          <div ref="trendChartRef" class="chart-box"></div>
        </div>
      </el-col>

      <!-- 支出分类饼图 -->
      <el-col :xs="24" :lg="10">
        <div class="chart-card">
          <div class="card-title">支出分类占比</div>
          <div ref="pieChartRef" class="chart-box"></div>
        </div>
      </el-col>
    </el-row>

    <!-- 信用卡还款明细 -->
    <div class="table-card">
      <div class="card-title">信用卡还款明细</div>
      <el-table :data="report.cardDetails || []" stripe border style="width:100%">
        <el-table-column prop="card_name" label="信用卡" />
        <el-table-column prop="bank_name" label="银行" width="120" />
        <el-table-column prop="bill_amount" label="账单金额">
          <template #default="{ row }">
            <span class="amount red">¥{{ formatNum(row.bill_amount) }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="actual_payment" label="实际还款">
          <template #default="{ row }">
            <span class="amount green">¥{{ formatNum(row.actual_payment) }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="repayment_status" label="状态" width="120">
          <template #default="{ row }">
            <el-tag :type="row.repayment_status === 1 ? 'success' : row.repayment_status === 2 ? 'warning' : 'danger'" size="small">
              {{ row.repayment_status === 1 ? '已还清' : row.repayment_status === 2 ? '部分还款' : '未还' }}
            </el-tag>
          </template>
        </el-table-column>
      </el-table>
      <el-empty v-if="!(report.cardDetails || []).length" description="本月暂无信用卡账单" :image-size="60" />
    </div>

    <!-- 支出分类统计 -->
    <div class="table-card">
      <div class="card-title">支出分类统计</div>
      <el-table :data="report.categoryStats || []" stripe style="width:100%">
        <el-table-column prop="category_name" label="分类" />
        <el-table-column prop="total" label="金额">
          <template #default="{ row }">
            <span class="amount red">¥{{ formatNum(row.total) }}</span>
          </template>
        </el-table-column>
        <el-table-column label="占比">
          <template #default="{ row }">
            <el-progress
              :percentage="categoryPercent(row.total)"
              :stroke-width="10"
              :format="() => categoryPercent(row.total) + '%'"
            />
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import * as echarts from 'echarts'
import { Refresh } from '@element-plus/icons-vue'
import { getMonthlySummary, getTrend } from '@/api/summary'

const trendChartRef = ref(null)
const pieChartRef = ref(null)
let trendChart = null
let pieChart = null

const now = new Date()
const selectedMonth = ref(`${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}`)

const report = ref({
  totalIncome: 0,
  totalExpense: 0,
  balance: 0,
  cardPaymentTotal: 0,
  cardDetails: [],
  categoryStats: []
})

function formatNum(v) { return Number(v || 0).toLocaleString('zh-CN', { minimumFractionDigits: 2 }) }
function disableFuture(date) { return date > new Date() }

function categoryPercent(total) {
  const expense = report.value.totalExpense || 0
  if (expense === 0) return 0
  return Math.round((total / expense) * 100)
}

function initTrendChart(data) {
  if (!trendChartRef.value) return
  trendChart?.dispose()
  trendChart = echarts.init(trendChartRef.value)
  trendChart.setOption({
    tooltip: { trigger: 'axis', axisPointer: { type: 'cross' } },
    legend: { data: ['收入', '支出', '结余'], bottom: 0 },
    grid: { top: 16, left: 8, right: 8, bottom: 40, containLabel: true },
    xAxis: { type: 'category', data: data.months, boundaryGap: false },
    yAxis: { type: 'value', axisLabel: { formatter: '¥{value}' } },
    series: [
      { name: '收入', type: 'line', data: data.incomes, smooth: true, lineStyle: { color: '#67c23a' }, itemStyle: { color: '#67c23a' } },
      { name: '支出', type: 'line', data: data.expenses, smooth: true, lineStyle: { color: '#f56c6c' }, itemStyle: { color: '#f56c6c' } },
      { name: '结余', type: 'line', data: data.balances, smooth: true, lineStyle: { color: '#409eff', type: 'dashed' }, itemStyle: { color: '#409eff' } }
    ]
  })
}

function initPieChart(categories) {
  if (!pieChartRef.value) return
  pieChart?.dispose()
  pieChart = echarts.init(pieChartRef.value)
  pieChart.setOption({
    tooltip: { trigger: 'item', formatter: '{b}: ¥{c} ({d}%)' },
    legend: { orient: 'vertical', right: 10, top: 'center', textStyle: { fontSize: 12 } },
    series: [{
      type: 'pie',
      radius: ['35%', '65%'],
      center: ['38%', '50%'],
      data: categories.map(c => ({ name: c.category_name, value: Number(c.total) })),
      label: { show: false },
      emphasis: { label: { show: true, fontWeight: 'bold' } }
    }],
    color: ['#409eff', '#67c23a', '#e6a23c', '#f56c6c', '#909399', '#9c59b6', '#1abc9c', '#e74c3c', '#3498db']
  })
}

function handleResize() { trendChart?.resize(); pieChart?.resize() }

async function loadReport() {
  try {
    const res = await getMonthlySummary({ month: selectedMonth.value })
    if (res.data) {
      report.value = res.data
    }
  } catch { /* keep defaults */ }

  // 渲染饼图
  setTimeout(() => {
    if (report.value.categoryStats?.length) {
      initPieChart(report.value.categoryStats)
    }
  }, 100)
}

onMounted(async () => {
  await loadReport()

  // 加载趋势数据
  try {
    const res = await getTrend()
    if (res.data) {
      setTimeout(() => initTrendChart(res.data), 100)
    }
  } catch { /* ignore */ }

  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  trendChart?.dispose()
  pieChart?.dispose()
})
</script>

<style scoped>
.page-wrap { display: flex; flex-direction: column; gap: 20px; }

.toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #ffffff;
  padding: 16px 20px;
  border-radius: 12px;
  box-shadow: 0 1px 6px rgba(0,0,0,0.06);
}

.filter-group { display: flex; align-items: center; gap: 10px; }
.filter-label { font-size: 14px; color: #606266; white-space: nowrap; }

.overview-card {
  background: #ffffff;
  border-radius: 12px;
  padding: 20px 24px;
  box-shadow: 0 1px 6px rgba(0,0,0,0.06);
  border-left: 4px solid transparent;
  text-align: center;
}

.overview-card.income { border-left-color: #67c23a; }
.overview-card.expense { border-left-color: #f56c6c; }
.overview-card.positive { border-left-color: #67c23a; }
.overview-card.negative { border-left-color: #f56c6c; }
.overview-card.payment { border-left-color: #e6a23c; }

.ov-label { font-size: 13px; color: #909399; margin-bottom: 4px; }
.ov-value { font-size: 22px; font-weight: 700; color: #1a1f2e; }

.chart-card, .table-card {
  background: #ffffff;
  border-radius: 12px;
  padding: 20px 24px;
  box-shadow: 0 1px 6px rgba(0,0,0,0.06);
}

.card-title {
  font-size: 15px;
  font-weight: 600;
  color: #1a1f2e;
  margin-bottom: 16px;
}

.chart-box { height: 260px; }

.amount { font-weight: 600; }
.amount.red { color: #f56c6c; }
.amount.green { color: #67c23a; }

@media (max-width: 768px) {
  .overview-card { margin-bottom: 16px; }
}
</style>
