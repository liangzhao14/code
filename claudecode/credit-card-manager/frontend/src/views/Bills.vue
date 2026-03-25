<template>
  <div class="page-wrap">
    <!-- 工具栏 -->
    <div class="toolbar">
      <div class="filter-group">
        <el-select v-model="query.cardId" placeholder="全部信用卡" clearable style="width:160px" @change="loadData">
          <el-option v-for="c in cardOptions" :key="c.id" :label="`${c.bankName} (${c.cardLastFour})`" :value="c.id" />
        </el-select>
        <el-date-picker
          v-model="query.month"
          type="month"
          placeholder="账期月份"
          format="YYYY-MM"
          value-format="YYYY-MM"
          style="width:140px"
          clearable
          @change="loadData"
        />
      </div>
      <el-button type="primary" :icon="Plus" @click="openDialog()">新增账单</el-button>
    </div>

    <!-- 数据表格 -->
    <div class="table-card">
      <el-table :data="bills" v-loading="loading" stripe border style="width:100%">
        <el-table-column label="信用卡" min-width="140">
          <template #default="{ row }">
            {{ getCardName(row.cardId) }}
          </template>
        </el-table-column>
        <el-table-column prop="billMonth" label="账期" width="100" />
        <el-table-column prop="billAmount" label="账单金额" width="130">
          <template #default="{ row }">
            <span class="amount red">¥{{ formatNum(row.billAmount) }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="minimumPayment" label="最低还款" width="120">
          <template #default="{ row }">
            <span v-if="row.minimumPayment">¥{{ formatNum(row.minimumPayment) }}</span>
            <span v-else class="text-muted">-</span>
          </template>
        </el-table-column>
        <el-table-column prop="actualPayment" label="实际还款" width="120">
          <template #default="{ row }">
            <span v-if="row.actualPayment" class="amount green">¥{{ formatNum(row.actualPayment) }}</span>
            <span v-else class="text-muted">-</span>
          </template>
        </el-table-column>
        <el-table-column prop="paymentDate" label="还款日期" width="120" />
        <el-table-column prop="repaymentStatus" label="状态" width="110">
          <template #default="{ row }">
            <el-tag :type="statusType(row.repaymentStatus)" size="small">
              {{ statusText(row.repaymentStatus) }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="200" fixed="right">
          <template #default="{ row }">
            <el-button size="small" @click="openDialog(row)">编辑</el-button>
            <el-button
              v-if="row.repaymentStatus !== 1"
              size="small"
              type="success"
              @click="handleMarkPaid(row)"
            >标记已还</el-button>
            <el-button size="small" type="danger" @click="handleDelete(row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <!-- 新增/编辑弹窗 -->
    <el-dialog v-model="dialogVisible" :title="editing ? '编辑账单' : '新增账单'" width="500px" :close-on-click-modal="false">
      <el-form ref="formRef" :model="form" :rules="rules" label-width="100px">
        <el-form-item label="信用卡" prop="cardId">
          <el-select v-model="form.cardId" placeholder="请选择" style="width:100%">
            <el-option v-for="c in cardOptions" :key="c.id" :label="`${c.bankName} (${c.cardLastFour})`" :value="c.id" />
          </el-select>
        </el-form-item>
        <el-form-item label="账期" prop="billMonth">
          <el-date-picker v-model="form.billMonth" type="month" format="YYYY-MM" value-format="YYYY-MM" style="width:100%" />
        </el-form-item>
        <el-form-item label="账单金额" prop="billAmount">
          <el-input-number v-model="form.billAmount" :min="0" :precision="2" controls-position="right" style="width:100%" />
        </el-form-item>
        <el-form-item label="最低还款额">
          <el-input-number v-model="form.minimumPayment" :min="0" :precision="2" controls-position="right" style="width:100%" />
        </el-form-item>
        <el-form-item label="还款状态">
          <el-radio-group v-model="form.repaymentStatus">
            <el-radio :value="0">未还</el-radio>
            <el-radio :value="1">已还</el-radio>
            <el-radio :value="2">部分还款</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="实际还款额" v-if="form.repaymentStatus !== 0">
          <el-input-number v-model="form.actualPayment" :min="0" :precision="2" controls-position="right" style="width:100%" />
        </el-form-item>
        <el-form-item label="还款日期" v-if="form.repaymentStatus !== 0">
          <el-date-picker v-model="form.paymentDate" type="date" format="YYYY-MM-DD" value-format="YYYY-MM-DD" style="width:100%" />
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
import { ref, reactive, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'
import { getBills, createBill, updateBill, deleteBill } from '@/api/bills'
import { getCards } from '@/api/cards'

const bills = ref([])
const loading = ref(false)
const dialogVisible = ref(false)
const submitting = ref(false)
const editing = ref(null)
const formRef = ref(null)
const cardOptions = ref([])

const query = reactive({ cardId: '', month: '' })

const form = reactive({
  cardId: '',
  billMonth: '',
  billAmount: 0,
  minimumPayment: null,
  repaymentStatus: 0,
  actualPayment: null,
  paymentDate: ''
})

const rules = {
  cardId: [{ required: true, message: '请选择信用卡', trigger: 'change' }],
  billMonth: [{ required: true, message: '请选择账期', trigger: 'change' }],
  billAmount: [{ required: true, message: '请输入账单金额', trigger: 'blur' }]
}

function formatNum(v) { return Number(v || 0).toLocaleString('zh-CN', { minimumFractionDigits: 2 }) }

function statusText(s) { return s === 1 ? '已还' : s === 2 ? '部分还款' : '未还' }
function statusType(s) { return s === 1 ? 'success' : s === 2 ? 'warning' : 'danger' }

function getCardName(cardId) {
  const card = cardOptions.value.find(c => c.id === cardId)
  return card ? `${card.bankName} (${card.cardLastFour})` : cardId
}

async function loadData() {
  loading.value = true
  try {
    const params = {}
    if (query.cardId) params.cardId = query.cardId
    if (query.month) params.month = query.month
    const res = await getBills(params)
    bills.value = res.data || []
  } catch { /* ignore */ } finally { loading.value = false }
}

async function loadCards() {
  try {
    const res = await getCards()
    cardOptions.value = res.data || []
  } catch { /* ignore */ }
}

function openDialog(row = null) {
  editing.value = row
  if (row) {
    Object.assign(form, {
      cardId: row.cardId,
      billMonth: row.billMonth,
      billAmount: row.billAmount,
      minimumPayment: row.minimumPayment,
      repaymentStatus: row.repaymentStatus,
      actualPayment: row.actualPayment,
      paymentDate: row.paymentDate
    })
  } else {
    Object.assign(form, { cardId: '', billMonth: '', billAmount: 0, minimumPayment: null, repaymentStatus: 0, actualPayment: null, paymentDate: '' })
  }
  dialogVisible.value = true
  formRef.value?.clearValidate()
}

async function handleSubmit() {
  const valid = await formRef.value?.validate().catch(() => false)
  if (!valid) return
  submitting.value = true
  try {
    if (editing.value) {
      await updateBill(editing.value.id, form)
      ElMessage.success('更新成功')
    } else {
      await createBill(form)
      ElMessage.success('新增成功')
    }
    dialogVisible.value = false
    loadData()
  } catch { /* ignore */ } finally { submitting.value = false }
}

async function handleMarkPaid(row) {
  await ElMessageBox.confirm(`确认将该账单标记为已还款？金额 ¥${formatNum(row.billAmount)}`, '确认还款', { type: 'info' })
  try {
    const today = new Date().toISOString().slice(0, 10)
    await updateBill(row.id, { ...row, repaymentStatus: 1, actualPayment: row.billAmount, paymentDate: today })
    ElMessage.success('标记还款成功')
    loadData()
  } catch { /* ignore */ }
}

async function handleDelete(row) {
  await ElMessageBox.confirm('确定删除该账单？', '警告', { type: 'warning' })
  try {
    await deleteBill(row.id)
    ElMessage.success('删除成功')
    loadData()
  } catch { /* ignore */ }
}

onMounted(() => { loadCards(); loadData() })
</script>

<style scoped>
.page-wrap { display: flex; flex-direction: column; gap: 20px; }

.toolbar {
  display: flex; align-items: center; justify-content: space-between;
  background: #ffffff; padding: 16px 20px; border-radius: 12px;
  box-shadow: 0 1px 6px rgba(0,0,0,0.06); flex-wrap: wrap; gap: 12px;
}

.filter-group { display: flex; gap: 10px; flex-wrap: wrap; }

.table-card {
  background: #ffffff; border-radius: 12px; padding: 20px;
  box-shadow: 0 1px 6px rgba(0,0,0,0.06);
}

.amount { font-weight: 600; }
.amount.red { color: #f56c6c; }
.amount.green { color: #67c23a; }
.text-muted { color: #c0c4cc; }
</style>
