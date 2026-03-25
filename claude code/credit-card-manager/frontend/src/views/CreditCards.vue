<template>
  <div class="page-wrap">
    <!-- 顶部操作栏 -->
    <div class="toolbar">
      <span class="total-info">共 {{ cards.length }} 张信用卡</span>
      <el-button type="primary" :icon="Plus" @click="openDialog()">新增信用卡</el-button>
    </div>

    <!-- 卡片列表 -->
    <el-row :gutter="20" v-loading="loading">
      <el-col
        v-for="card in cards"
        :key="card.id"
        :xs="24" :sm="12" :lg="8" :xl="6"
        class="card-col"
      >
        <div class="credit-card" :style="{ background: cardGradients[card.id % cardGradients.length] }">
          <div class="cc-header">
            <span class="cc-bank">{{ card.bankName }}</span>
            <el-icon class="cc-chip"><CreditCard /></el-icon>
          </div>
          <div class="cc-number">**** **** **** {{ card.cardLastFour || '0000' }}</div>
          <div class="cc-footer">
            <div>
              <p class="cc-label">卡名称</p>
              <p class="cc-val">{{ card.cardName }}</p>
            </div>
            <div class="text-right">
              <p class="cc-label">信用额度</p>
              <p class="cc-val">¥{{ formatNumber(card.creditLimit) }}</p>
            </div>
          </div>
          <div class="cc-info-row">
            <el-tag size="small" effect="dark" color="rgba(255,255,255,0.2)" style="color:#fff;border:none">
              账单日 {{ card.billingDay }}日
            </el-tag>
            <el-tag size="small" effect="dark" color="rgba(255,255,255,0.2)" style="color:#fff;border:none">
              还款日 {{ card.dueDay }}日
            </el-tag>
          </div>
          <div class="cc-actions">
            <el-button size="small" type="primary" plain @click="openDialog(card)">编辑</el-button>
            <el-button size="small" type="danger" plain @click="handleDelete(card)">删除</el-button>
          </div>
        </div>
      </el-col>

      <el-col v-if="!loading && cards.length === 0" :span="24">
        <el-empty description="暂无信用卡，点击右上角新增" />
      </el-col>
    </el-row>

    <!-- 新增/编辑弹窗 -->
    <el-dialog
      v-model="dialogVisible"
      :title="editingCard ? '编辑信用卡' : '新增信用卡'"
      width="500px"
      :close-on-click-modal="false"
    >
      <el-form ref="formRef" :model="form" :rules="rules" label-width="90px">
        <el-form-item label="卡名称" prop="cardName">
          <el-input v-model="form.cardName" placeholder="如：招行金卡" />
        </el-form-item>
        <el-form-item label="银行名称" prop="bankName">
          <el-input v-model="form.bankName" placeholder="如：招商银行" />
        </el-form-item>
        <el-form-item label="卡号后四位" prop="cardLastFour">
          <el-input v-model="form.cardLastFour" maxlength="4" placeholder="如：8888" />
        </el-form-item>
        <el-form-item label="信用额度" prop="creditLimit">
          <el-input-number v-model="form.creditLimit" :min="0" :precision="2" style="width:100%" controls-position="right" />
        </el-form-item>
        <el-form-item label="账单日" prop="billingDay">
          <el-input-number v-model="form.billingDay" :min="1" :max="31" style="width:100%" controls-position="right" />
        </el-form-item>
        <el-form-item label="还款日" prop="dueDay">
          <el-input-number v-model="form.dueDay" :min="1" :max="31" style="width:100%" controls-position="right" />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" :loading="submitting" @click="handleSubmit">
          {{ editingCard ? '保存' : '新增' }}
        </el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'
import { getCards, createCard, updateCard, deleteCard } from '@/api/cards'

const cards = ref([])
const loading = ref(false)
const dialogVisible = ref(false)
const submitting = ref(false)
const editingCard = ref(null)
const formRef = ref(null)

const cardGradients = [
  'linear-gradient(135deg, #1a1f2e, #2d4a8a)',
  'linear-gradient(135deg, #1a3a2a, #2d7a4a)',
  'linear-gradient(135deg, #3a1a1a, #8a2d2d)',
  'linear-gradient(135deg, #2a1a3a, #6a2d8a)',
  'linear-gradient(135deg, #1a2a3a, #2d6a8a)',
  'linear-gradient(135deg, #3a2a1a, #8a6a2d)'
]

const form = reactive({
  cardName: '',
  bankName: '',
  cardLastFour: '',
  creditLimit: 10000,
  billingDay: 1,
  dueDay: 20
})

const rules = {
  cardName: [{ required: true, message: '请输入卡名称', trigger: 'blur' }],
  bankName: [{ required: true, message: '请输入银行名称', trigger: 'blur' }],
  cardLastFour: [{ required: true, message: '请输入卡号后四位', trigger: 'blur' }],
  creditLimit: [{ required: true, message: '请输入信用额度', trigger: 'blur' }],
  billingDay: [{ required: true, message: '请输入账单日', trigger: 'blur' }],
  dueDay: [{ required: true, message: '请输入还款日', trigger: 'blur' }]
}

function formatNumber(val) {
  return Number(val || 0).toLocaleString('zh-CN')
}

async function loadCards() {
  loading.value = true
  try {
    const res = await getCards()
    cards.value = res.data || []
  } catch { /* ignore */ } finally {
    loading.value = false
  }
}

function openDialog(card = null) {
  editingCard.value = card
  if (card) {
    Object.assign(form, { cardName: card.cardName, bankName: card.bankName, cardLastFour: card.cardLastFour, creditLimit: card.creditLimit, billingDay: card.billingDay, dueDay: card.dueDay })
  } else {
    Object.assign(form, { cardName: '', bankName: '', cardLastFour: '', creditLimit: 10000, billingDay: 1, dueDay: 20 })
  }
  dialogVisible.value = true
  formRef.value?.clearValidate()
}

async function handleSubmit() {
  const valid = await formRef.value?.validate().catch(() => false)
  if (!valid) return
  submitting.value = true
  try {
    if (editingCard.value) {
      await updateCard(editingCard.value.id, form)
      ElMessage.success('更新成功')
    } else {
      await createCard(form)
      ElMessage.success('新增成功')
    }
    dialogVisible.value = false
    loadCards()
  } catch { /* ignore */ } finally {
    submitting.value = false
  }
}

async function handleDelete(card) {
  await ElMessageBox.confirm(`确定删除 ${card.cardName}（${card.bankName}）吗？`, '警告', {
    type: 'warning',
    confirmButtonText: '删除',
    confirmButtonClass: 'el-button--danger'
  })
  try {
    await deleteCard(card.id)
    ElMessage.success('删除成功')
    loadCards()
  } catch { /* ignore */ }
}

onMounted(loadCards)
</script>

<style scoped>
.page-wrap { display: flex; flex-direction: column; gap: 20px; }

.toolbar {
  display: flex; align-items: center; justify-content: space-between;
  background: #ffffff; padding: 16px 20px; border-radius: 12px;
  box-shadow: 0 1px 6px rgba(0,0,0,0.06);
}

.total-info { font-size: 14px; color: #606266; }
.card-col { margin-bottom: 20px; }

.credit-card {
  border-radius: 16px; padding: 20px; color: #fff;
  min-height: 200px; display: flex; flex-direction: column; gap: 12px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.2);
  transition: transform 0.2s, box-shadow 0.2s;
}

.credit-card:hover { transform: translateY(-4px); box-shadow: 0 12px 32px rgba(0,0,0,0.25); }

.cc-header { display: flex; justify-content: space-between; align-items: center; }
.cc-bank { font-size: 16px; font-weight: 700; letter-spacing: 0.5px; }
.cc-chip { font-size: 24px; opacity: 0.8; }
.cc-number { font-size: 18px; font-family: monospace; letter-spacing: 2px; opacity: 0.9; }
.cc-footer { display: flex; justify-content: space-between; align-items: flex-end; }
.cc-label { font-size: 11px; opacity: 0.6; margin-bottom: 2px; }
.cc-val { font-size: 14px; font-weight: 600; }
.text-right { text-align: right; }
.cc-info-row { display: flex; gap: 8px; }
.cc-actions { display: flex; gap: 8px; margin-top: 4px; }
.cc-actions .el-button { flex: 1; }
</style>
