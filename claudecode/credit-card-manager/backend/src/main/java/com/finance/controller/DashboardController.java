package com.finance.controller;

import com.finance.dto.Result;
import com.finance.entity.CreditCard;
import com.finance.service.CreditCardService;
import com.finance.service.ExpenseService;
import com.finance.service.IncomeService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.YearMonth;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/dashboard")
@RequiredArgsConstructor
public class DashboardController {

    private final IncomeService incomeService;
    private final ExpenseService expenseService;
    private final CreditCardService creditCardService;

    /**
     * 首页看板数据：
     *   - monthOverview：本月收入/支出/结余
     *   - upcomingPayments：未来7天内需还款的信用卡列表
     *   - comparison：本月 vs 上月的收入和支出对比
     */
    @GetMapping
    public Result<Map<String, Object>> dashboard() {
        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM");
        LocalDate today = LocalDate.now();
        String currentMonth = YearMonth.now().format(fmt);
        String lastMonth = YearMonth.now().minusMonths(1).format(fmt);

        // --- 本月概览 ---
        BigDecimal income = incomeService.sumByMonth(currentMonth);
        BigDecimal expense = expenseService.sumByMonth(currentMonth);
        BigDecimal balance = income.subtract(expense);

        Map<String, Object> monthOverview = new HashMap<>();
        monthOverview.put("income", income);
        monthOverview.put("expense", expense);
        monthOverview.put("balance", balance);
        monthOverview.put("month", currentMonth);

        // --- 未来7天待还信用卡 ---
        List<CreditCard> allCards = creditCardService.list();
        List<Map<String, Object>> upcomingPayments = new ArrayList<>();

        for (CreditCard card : allCards) {
            if (card.getDueDay() == null) continue;

            // 在当前月份内构造还款日，若还款日已过则查下个月
            LocalDate dueDate = buildNearestDueDate(today, card.getDueDay());

            long daysUntilDue = today.until(dueDate, java.time.temporal.ChronoUnit.DAYS);
            if (daysUntilDue >= 0 && daysUntilDue <= 7) {
                Map<String, Object> item = new HashMap<>();
                item.put("cardId", card.getId());
                item.put("cardName", card.getCardName());
                item.put("bankName", card.getBankName());
                item.put("cardLastFour", card.getCardLastFour());
                item.put("dueDay", card.getDueDay());
                item.put("dueDate", dueDate.toString());
                item.put("daysUntilDue", daysUntilDue);
                upcomingPayments.add(item);
            }
        }

        // --- 本月 vs 上月对比 ---
        BigDecimal lastIncome = incomeService.sumByMonth(lastMonth);
        BigDecimal lastExpense = expenseService.sumByMonth(lastMonth);

        Map<String, Object> comparison = new HashMap<>();
        comparison.put("currentMonth", currentMonth);
        comparison.put("lastMonth", lastMonth);
        comparison.put("currentIncome", income);
        comparison.put("lastIncome", lastIncome);
        comparison.put("currentExpense", expense);
        comparison.put("lastExpense", lastExpense);
        comparison.put("incomeDiff", income.subtract(lastIncome));
        comparison.put("expenseDiff", expense.subtract(lastExpense));

        Map<String, Object> result = new HashMap<>();
        result.put("monthOverview", monthOverview);
        result.put("upcomingPayments", upcomingPayments);
        result.put("comparison", comparison);

        return Result.ok(result);
    }

    /**
     * 根据今天日期和还款日（dueDay），计算距今最近的未来（含今天）还款日。
     * 若本月还款日未到或就是今天，返回本月还款日；否则返回下个月的还款日。
     */
    private LocalDate buildNearestDueDate(LocalDate today, int dueDay) {
        YearMonth currentYM = YearMonth.from(today);
        int maxDay = currentYM.lengthOfMonth();
        int actualDay = Math.min(dueDay, maxDay);
        LocalDate dueThisMonth = currentYM.atDay(actualDay);

        if (!dueThisMonth.isBefore(today)) {
            return dueThisMonth;
        }

        YearMonth nextYM = currentYM.plusMonths(1);
        int nextMaxDay = nextYM.lengthOfMonth();
        int nextActualDay = Math.min(dueDay, nextMaxDay);
        return nextYM.atDay(nextActualDay);
    }
}
