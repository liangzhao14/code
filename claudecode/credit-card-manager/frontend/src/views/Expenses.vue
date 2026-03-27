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
        <el-select v-model="query.categoryId" placeholder="支出分类" clearable style="width:130px" @change="loadData">
          <el-option v-for="c in categories" :key="c.id" :label="c.name" :value="c.id" />
        </el-select>
      </div>
      <el-button type="primary" :icon="Plus" @click="openDialog()">新增支出</el-button>
    </div>

    <!-- 汇总卡片 -->
    <el-row :gutter="16">
      <el-col :span="8">
        <div class="summary-card red">
          <p class="s-label">本页总支出</p>
          <p class="s-value">¥{{ formatNum(summary.total) }}</p>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="summary-card blue">
          <p class="s-label">支出笔数</p>
          <p class="s-value">{{ summary.count }} 笔</p>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="summary-card orange">
          <p class="s-label">最大单笔</p>
          <p class="s-value">¥{{ formatNum(summary.maxAmount) }}</p>
        </div>
      </el-col>
    </el-row>

    <!-- 数据表格 -->
    <div class="table-card">
      <el-table :data="expenses" v-loading="loading" stripe border style="width:100%">
        <el-table-column prop="expenseDate" label="支出日期" width="120" />
        <el-table-column label="分类" width="100">
          <template #default="{ row }">
            <el-tag size="small" type="warning">{{ getCategoryName(row.categoryId) }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="amount" label="金额" width="130">
          <template #default="{ row }">
            <span class="amount red">-¥{{ formatNum(row.amount) }}</span>
          </template>
        </el-table-column>
        <el-table-column label="关联信用卡" width="150">
          <template #default="{ row }">
            <span v-if="row.cardId">{{ getCardName(row.cardId) }}</span>
            <span v-else class="text-muted">-</span>
          </template>
        </el-table-column>
        <el-table-column prop="remark" label="备注" min-width="160" show-overflow-tooltip />
        <el-table-column label="操作" width="140" fixed="right">
          <template #default="{ row }">
            <el-button size="small" @click="openDialog(row)">编辑</el-button>
            <el-button size="small" type="danger" @click="handleDelete(row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <!-- 弹窗 -->
    <el-dialog v-model="dialogVisible" :title="editing ? '编辑支出' : '新增支出'" width="480px" :close-on-click-modal="false">
      <el-form ref="formRef" :model="form" :rules="rules" label-width="90px">
        <el-form-item label="支出日期" prop="expenseDate">
          <el-date-picker v-model="form.expenseDate" type="date" format="YYYY-MM-DD" value-format="YYYY-MM-DD" style="width:100%" />
        </el-form-item>
        <el-form-item label="分类" prop="categoryId">
          <el-select v-model="form.categoryId" placeholder="请选择" style="width:100%">
            <el-option v-for="c in categories" :key="c.id" :label="c.name" :value="c.id" />
          </el-select>
        </el-form-item>
        <el-form-item label="金额" prop="amount">
          <el-input-number v-model="form.amount" :min="0" :precision="2" controls-position="right" style="width:100%" />
        </el-form-item>
        <el-form-item label="关联信用卡">
          <el-select v-model="form.cardId" placeholder="可选" clearable style="width:100%">
            <el-option v-for="c in cardOptions" :key="c.id" :label="`${c.bankName} (${c.cardLastFour})`" :value="c.id" />
          </el-select>
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
import { getExpenses, createExpense, updateExpense, deleteExpense } from '@/api/expenses'
import { getCategories } from '@/api/categories'
import { getCards } from '@/api/cards'

const expenses = ref([])
const loading = ref(false)
const dialogVisible = ref(false)
const submitting = ref(false)
const editing = ref(null)
const formRef = ref(null)
const categories = ref([])
const cardOptions = ref([])

const query = reactive({ month: '', categoryId: '' })
const form = reactive({ expenseDate: '', categoryId: '', amount: 0, cardId: '', remark: '' })

const rules = {
  expenseDate: [{ required: true, message: '请选择日期', trigger: 'change' }],
  categoryId: [{ required: true, message: '请选择分类', trigger: 'change' }],
  amount: [{ required: true, message: '请输入金额', trigger: 'blur' }]
}

const summary = computed(() => {
  const list = expenses.value
  const t = list.reduce((s, r) => s + (r.amount || 0), 0)
  const max = list.length ? Math.max(...list.map(r => r.amount || 0)) : 0
  return { total: t, count: list.length, maxAmount: max }
})

function formatNum(v) { return Number(v || 0).toLocaleString('zh-CN', { minimumFractionDigits: 2 }) }

function getCategoryName(categoryId) {
  const cat = categories.value.find(c => c.id === categoryId)
  return cat ? cat.name : '未知'
}

function getCardName(cardId) {
  const card = cardOptions.value.find(c => c.id === cardId)
  return card ? `${card.bankName} (${card.cardLastFour})` : ''
}

async function loadData() {
  loading.value = true
  try {
    const params = {}
    if (query.month) params.month = query.month
    if (query.categoryId) params.categoryId = query.categoryId
    const res = await getExpenses(params)
    expenses.value = res.data || []
  } catch { /* ignore */ } finally { loading.value = false }
}

async function loadOptions() {
  try {
    const [cRes, kRes] = await Promise.all([getCategories(), getCards()])
    categories.value = cRes.data || []
    cardOptions.value = kRes.data || []
  } catch { /* ignore */ }
}

function openDialog(row = null) {
  editing.value = row
  if (row) {
    Object.assign(form, { expenseDate: row.expenseDate, categoryId: row.categoryId, amount: row.amount, cardId: row.cardId || '', remark: row.remark })
  } else {
    Object.assign(form, { expenseDate: '', categoryId: '', amount: 0, cardId: '', remark: '' })
  }
  dialogVisible.value = true
  formRef.value?.clearValidate()
}

async function handleSubmit() {
  const valid = await formRef.value?.validate().catch(() => false)
  if (!valid) return
  submitting.value = true
  try {
    const data = { ...form }
    if (!data.cardId) data.cardId = null
    if (editing.value) { await updateExpense(editing.value.id, data); ElMessage.success('更新成功') }
    else { await createExpense(data); ElMessage.success('新增成功') }
    dialogVisible.value = false
    loadData()
  } catch { /* ignore */ } finally { submitting.value = false }
}

async function handleDelete(row) {
  await ElMessageBox.confirm('确定删除该支出记录？', '警告', { type: 'warning' })
  try { await deleteExpense(row.id); ElMessage.success('删除成功'); loadData() } catch { /* ignore */ }
}

onMounted(() => { loadOptions(); loadData() })
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

.summary-card.red { border-top-color: #f56c6c; }
.summary-card.blue { border-top-color: #409eff; }
.summary-card.orange { border-top-color: #e6a23c; }

.s-label { font-size: 13px; color: #909399; margin-bottom: 8px; }
.s-value { font-size: 22px; font-weight: 700; color: #1a1f2e; }

.table-card {
  background: #ffffff; border-radius: 12px; padding: 20px;
  box-shadow: 0 1px 6px rgba(0,0,0,0.06);
}

.amount { font-weight: 600; }
.amount.red { color: #f56c6c; }
.text-muted { color: #c0c4cc; }
</style>
