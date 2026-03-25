package com.finance.service.impl;

import com.finance.service.CreditCardBillService;
import com.finance.service.ExpenseService;
import com.finance.service.IncomeService;
import com.finance.service.SummaryService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.time.YearMonth;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
@RequiredArgsConstructor
public class SummaryServiceImpl implements SummaryService {

    private final IncomeService incomeService;
    private final ExpenseService expenseService;
    private final CreditCardBillService creditCardBillService;

    @Override
    public Map<String, Object> getMonthlySummary(String month) {
        BigDecimal totalIncome = incomeService.sumByMonth(month);
        BigDecimal totalExpense = expenseService.sumByMonth(month);
        BigDecimal cardPaymentTotal = creditCardBillService.sumPaymentByMonth(month);
        BigDecimal balance = totalIncome.subtract(totalExpense);

        List<Map<String, Object>> cardDetails = creditCardBillService.getBillDetailsByMonth(month);
        List<Map<String, Object>> categoryStats = expenseService.sumByCategoryAndMonth(month);

        Map<String, Object> result = new HashMap<>();
        result.put("totalIncome", totalIncome);
        result.put("totalExpense", totalExpense);
        result.put("balance", balance);
        result.put("cardPaymentTotal", cardPaymentTotal);
        result.put("cardDetails", cardDetails);
        result.put("categoryStats", categoryStats);
        return result;
    }

    @Override
    public Map<String, Object> getTrend() {
        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM");
        YearMonth current = YearMonth.now();

        List<String> months = new ArrayList<>();
        List<BigDecimal> incomes = new ArrayList<>();
        List<BigDecimal> expenses = new ArrayList<>();
        List<BigDecimal> balances = new ArrayList<>();

        for (int i = 5; i >= 0; i--) {
            YearMonth ym = current.minusMonths(i);
            String monthStr = ym.format(fmt);
            months.add(monthStr);

            BigDecimal income = incomeService.sumByMonth(monthStr);
            BigDecimal expense = expenseService.sumByMonth(monthStr);
            BigDecimal balance = income.subtract(expense);

            incomes.add(income);
            expenses.add(expense);
            balances.add(balance);
        }

        Map<String, Object> result = new HashMap<>();
        result.put("months", months);
        result.put("incomes", incomes);
        result.put("expenses", expenses);
        result.put("balances", balances);
        return result;
    }
}
