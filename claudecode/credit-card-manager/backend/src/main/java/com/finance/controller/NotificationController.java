package com.finance.controller;

import com.finance.dto.Result;
import com.finance.entity.CreditCard;
import com.finance.entity.CreditCardBill;
import com.finance.service.CreditCardBillService;
import com.finance.service.CreditCardService;
import com.finance.service.ExpenseService;
import com.finance.service.IncomeService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.YearMonth;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.util.*;

@RestController
@RequestMapping("/api/notifications")
@RequiredArgsConstructor
public class NotificationController {

    private final CreditCardService creditCardService;
    private final CreditCardBillService creditCardBillService;
    private final IncomeService incomeService;
    private final ExpenseService expenseService;

    @GetMapping
    public Result<Map<String, Object>> getNotifications() {
        List<Map<String, Object>> notifications = new ArrayList<>();
        LocalDate today = LocalDate.now();
        String currentMonth = YearMonth.now().format(DateTimeFormatter.ofPattern("yyyy-MM"));

        // === 1. 还款提醒：7天内到期且未还清的账单 ===
        List<CreditCard> allCards = creditCardService.list();
        List<CreditCardBill> currentBills = creditCardBillService.listByMonth(currentMonth);

        for (CreditCard card : allCards) {
            if (card.getDueDay() == null) continue;

            LocalDate dueDate = buildNearestDueDate(today, card.getDueDay());
            long daysUntilDue = ChronoUnit.DAYS.between(today, dueDate);

            if (daysUntilDue < 0 || daysUntilDue > 7) continue;

            // 查找该卡本月账单中未还清的
            Optional<CreditCardBill> unpaidBill = currentBills.stream()
                    .filter(b -> b.getCardId().equals(card.getId()))
                    .filter(b -> b.getRepaymentStatus() == null || b.getRepaymentStatus() != 1)
                    .findFirst();

            if (unpaidBill.isEmpty()) continue;

            Map<String, Object> n = new LinkedHashMap<>();
            n.put("type", "repayment");
            n.put("cardName", card.getCardName());
            n.put("bankName", card.getBankName());
            n.put("cardLastFour", card.getCardLastFour());
            n.put("dueDate", dueDate.toString());
            n.put("daysUntilDue", daysUntilDue);
            n.put("billAmount", unpaidBill.get().getBillAmount());
            n.put("repaymentStatus", unpaidBill.get().getRepaymentStatus());

            if (daysUntilDue == 0) {
                n.put("title", card.getCardName() + " 今天到期还款");
                n.put("level", "danger");
            } else if (daysUntilDue <= 3) {
                n.put("title", card.getCardName() + " " + daysUntilDue + "天后到期");
                n.put("level", "warning");
            } else {
                n.put("title", card.getCardName() + " " + daysUntilDue + "天后到期");
                n.put("level", "info");
            }
            notifications.add(n);
        }

        // === 2. 系统消息：本月收支概况 ===
        BigDecimal monthIncome = incomeService.sumByMonth(currentMonth);
        BigDecimal monthExpense = expenseService.sumByMonth(currentMonth);

        if (monthIncome.compareTo(BigDecimal.ZERO) > 0 || monthExpense.compareTo(BigDecimal.ZERO) > 0) {
            Map<String, Object> summary = new LinkedHashMap<>();
            summary.put("type", "system");
            summary.put("title", currentMonth + " 收支概况");
            summary.put("level", "info");
            summary.put("income", monthIncome);
            summary.put("expense", monthExpense);
            summary.put("balance", monthIncome.subtract(monthExpense));
            notifications.add(summary);
        }

        // === 3. 系统消息：逾期未还账单 ===
        for (CreditCard card : allCards) {
            if (card.getDueDay() == null) continue;

            LocalDate dueDate = buildNearestDueDate(today, card.getDueDay());
            // 如果最近还款日在今天之前（即上个月的还款日已过），检查是否有逾期
            // 用上个月来查
            String lastMonth = YearMonth.now().minusMonths(1).format(DateTimeFormatter.ofPattern("yyyy-MM"));
            List<CreditCardBill> lastBills = creditCardBillService.listByMonth(lastMonth);

            Optional<CreditCardBill> overdueBill = lastBills.stream()
                    .filter(b -> b.getCardId().equals(card.getId()))
                    .filter(b -> b.getRepaymentStatus() == null || b.getRepaymentStatus() == 0)
                    .findFirst();

            if (overdueBill.isPresent()) {
                Map<String, Object> n = new LinkedHashMap<>();
                n.put("type", "overdue");
                n.put("title", card.getCardName() + " " + lastMonth + " 账单逾期未还");
                n.put("level", "danger");
                n.put("cardName", card.getCardName());
                n.put("bankName", card.getBankName());
                n.put("billAmount", overdueBill.get().getBillAmount());
                n.put("billMonth", lastMonth);
                notifications.add(n);
            }
        }

        // 按优先级排序：danger > warning > info
        notifications.sort((a, b) -> {
            Map<String, Integer> priority = Map.of("danger", 0, "warning", 1, "info", 2);
            int pa = priority.getOrDefault(a.get("level"), 9);
            int pb = priority.getOrDefault(b.get("level"), 9);
            return Integer.compare(pa, pb);
        });

        int unreadCount = (int) notifications.stream()
                .filter(n -> !"system".equals(n.get("type")))
                .count();

        Map<String, Object> result = new LinkedHashMap<>();
        result.put("unreadCount", unreadCount);
        result.put("notifications", notifications);

        return Result.ok(result);
    }

    private LocalDate buildNearestDueDate(LocalDate today, int dueDay) {
        YearMonth currentYM = YearMonth.from(today);
        int actualDay = Math.min(dueDay, currentYM.lengthOfMonth());
        LocalDate dueThisMonth = currentYM.atDay(actualDay);

        if (!dueThisMonth.isBefore(today)) {
            return dueThisMonth;
        }

        YearMonth nextYM = currentYM.plusMonths(1);
        int nextActualDay = Math.min(dueDay, nextYM.lengthOfMonth());
        return nextYM.atDay(nextActualDay);
    }
}
