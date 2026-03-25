<template>
  <div class="page-wrap">
    <!-- 工具栏 -->
    <div class="toolbar">
      <div class="filter-group">
        <el-date-picker
          v-model="query.month"
          type="month"
          placeholder="筛选月份"
          format="YYYY-MM"
          value-format="YYYY-MM"
          style="width:140px"
          clearable
          @change="loadData"
        />
        <el-select v-model="filterType" placeholder="收入类型" clearable style="width:130px" @change="loadData">
          <el-option label="工资" value="工资" />
          <el-option label="奖金" value="奖金" />
          <el-option label="其他" value="其他" />
        </el-select>
      </div>
      <el-button type="primary" :icon="Plus" @click="openDialog()">新增收入</el-button>
    </div>

    <!-- 汇总卡片 -->
    <el-row :gutter="16">
      <el-col :span="8">
        <div class="summary-card green">
          <p class="s-label">本页总收入</p>
          <p class="s-value">¥{{ formatNum(monthlySummary.totalIncome) }}</p>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="summary-card blue">
          <p class="s-label">收入笔数</p>
          <p class="s-value">{{ monthlySummary.count }} 笔</p>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="summary-card orange">
          <p class="s-label">平均每笔</p>
          <p class="s-value">¥{{ formatNum(monthlySummary.avgAmount) }}</p>
        </div>
      </el-col>
    </el-row>

    <!-- 数据表格 -->
    <div class="table-card">
      <el-table :data="filteredIncomes" v-loading="loading" stripe border style="width:100%">
        <el-table-column prop="incomeDate" label="收入日期" width="120" />
        <el-table-column prop="incomeType" label="类型" width="100">
          <template #default="{ row }">
            <el-tag size="small" type="success">{{ row.incomeType }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="amount" label="金额" width="130">
          <template #default="{ row }">
            <span class="amount green">+¥{{ formatNum(row.amount) }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="remark" label="备注" min-width="200" show-overflow-tooltip />
        <el-table-column label="操作" width="140" fixed="right">
          <template #default="{ row }">
            <el-button size="small" @click="openDialog(row)">编辑</el-button>
            <el-button size="small" type="danger" @click="handleDelete(row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <!-- 弹窗 -->
    <el-dialog v-model="dialogVisible" :title="editing ? '编辑收入' : '新增收入'" width="460px" :close-on-click-modal="false">
      <el-form ref="formRef" :model="form" :rules="rules" label-width="90px">
        <el-form-item label="收入日期" prop="incomeDate">
          <el-date-picker v-model="form.incomeDate" type="date" format="YYYY-MM-DD" value-format="YYYY-MM-DD" style="width:100%" />
        </el-form-item>
        <el-form-item label="收入类型" prop="incomeType">
          <el-select v-model="form.incomeType" placeholder="请选择" style="width:100%">
            <el-option label="工资" value="工资" />
            <el-option label="奖金" value="奖金" />
            <el-option label="其他" value="其他" />
          </el-select>
        </el-form-item>
        <el-form-item label="金额" prop="amount">
          <el-input-number v-model="form.amount" :min="0" :precision="2" controls-position="right" style="width:100%" />
        </el-form-item>
        <el-form-item label="备注">
          <el-input v-model="form.remark" type="textarea" :rows="2" placeholder="可选" />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" :loading="submitting" @click="handleSubmit">保存</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'
import { getIncomes, createIncome, updateIncome, deleteIncome } from '@/api/incomes'

const incomes = ref([])
const loading = ref(false)
const dialogVisible = ref(false)
const submitting = ref(false)
const editing = ref(null)
const formRef = ref(null)
const filterType = ref('')

const query = reactive({ month: '' })
const form = reactive({ incomeDate: '', incomeType: '工资', amount: 0, remark: '' })

const rules = {
  incomeDate: [{ required: true, message: '请选择收入日期', trigger: 'change' }],
  incomeType: [{ required: true, message: '请选择收入类型', trigger: 'change' }],
  amount: [{ required: true, message: '请输入金额', trigger: 'blur' }]
}

const filteredIncomes = computed(() => {
  if (!filterType.value) return incomes.value
  return incomes.value.filter(i => i.incomeType === filterType.value)
})

const monthlySummary = computed(() => {
  const list = filteredIncomes.value
  const total = list.reduce((s, r) => s + (r.amount || 0), 0)
  const count = list.length
  return { totalIncome: total, count, avgAmount: count ? total / count : 0 }
})

function formatNum(v) { return Number(v || 0).toLocaleString('zh-CN', { minimumFractionDigits: 2 }) }

async function loadData() {
  loading.value = true
  try {
    const params = {}
    if (query.month) params.month = query.month
    const res = await getIncomes(params)
    incomes.value = res.data || []
  } catch { /* ignore */ } finally { loading.value = false }
}

function openDialog(row = null) {
  editing.value = row
  if (row) {
    Object.assign(form, { incomeDate: row.incomeDate, incomeType: row.incomeType, amount: row.amount, remark: row.remark })
  } else {
    Object.assign(form, { incomeDate: '', incomeType: '工资', amount: 0, remark: '' })
  }
  dialogVisible.value = true
  formRef.value?.clearValidate()
}

async function handleSubmit() {
  const valid = await formRef.value?.validate().catch(() => false)
  if (!valid) return
  submitting.value = true
  try {
    if (editing.value) { await updateIncome(editing.value.id, form); ElMessage.success('更新成功') }
    else { await createIncome(form); ElMessage.success('新增成功') }
    dialogVisible.value = false
    loadData()
  } catch { /* ignore */ } finally { submitting.value = false }
}

async function handleDelete(row) {
  await ElMessageBox.confirm('确定删除该条收入记录？', '警告', { type: 'warning' })
  try { await deleteIncome(row.id); ElMessage.success('删除成功'); loadData() } catch { /* ignore */ }
}

onMounted(loadData)
</script>

<style scoped>
.page-wrap { display: flex; flex-direction: column; gap: 20px; }

.toolbar {
  display: flex; align-items: center; justify-content: space-between;
  background: #ffffff; padding: 16px 20px; border-radius: 12px;
  box-shadow: 0 1px 6px rgba(0,0,0,0.06); flex-wrap: wrap; gap: 12px;
}

.filter-group { display: flex; gap: 10px; flex-wrap: wrap; }

.summary-card {
  background: #ffffff; border-radius: 12px; padding: 16px 20px;
  box-shadow: 0 1px 6px rgba(0,0,0,0.06); border-top: 3px solid transparent;
}

.summary-card.green { border-top-color: #67c23a; }
.summary-card.blue { border-top-color: #409eff; }
.summary-card.orange { border-top-color: #e6a23c; }

.s-label { font-size: 13px; color: #909399; margin-bottom: 8px; }
.s-value { font-size: 22px; font-weight: 700; color: #1a1f2e; }

.table-card {
  background: #ffffff; border-radius: 12px; padding: 20px;
  box-shadow: 0 1px 6px rgba(0,0,0,0.06);
}

.amount { font-weight: 600; }
.amount.green { color: #67c23a; }
</style>
