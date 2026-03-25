package com.finance.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.finance.entity.Expense;
import com.finance.mapper.ExpenseMapper;
import com.finance.service.ExpenseService;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.time.YearMonth;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.Map;

@Service
public class ExpenseServiceImpl extends ServiceImpl<ExpenseMapper, Expense>
        implements ExpenseService {

    @Override
    public List<Expense> listByMonth(String month) {
        YearMonth ym = YearMonth.parse(month, DateTimeFormatter.ofPattern("yyyy-MM"));
        return list(new LambdaQueryWrapper<Expense>()
                .ge(Expense::getExpenseDate, ym.atDay(1))
                .le(Expense::getExpenseDate, ym.atEndOfMonth())
                .orderByDesc(Expense::getExpenseDate));
    }

    @Override
    public List<Expense> listByCategoryId(Long categoryId) {
        return list(new LambdaQueryWrapper<Expense>()
                .eq(Expense::getCategoryId, categoryId)
                .orderByDesc(Expense::getExpenseDate));
    }

    @Override
    public List<Expense> listByCategoryAndMonth(Long categoryId, String month) {
        YearMonth ym = YearMonth.parse(month, DateTimeFormatter.ofPattern("yyyy-MM"));
        LambdaQueryWrapper<Expense> wrapper = new LambdaQueryWrapper<Expense>()
                .ge(Expense::getExpenseDate, ym.atDay(1))
                .le(Expense::getExpenseDate, ym.atEndOfMonth())
                .orderByDesc(Expense::getExpenseDate);
        if (categoryId != null) {
            wrapper.eq(Expense::getCategoryId, categoryId);
        }
        return list(wrapper);
    }

    @Override
    public BigDecimal sumByMonth(String month) {
        return baseMapper.sumByMonth(month);
    }

    @Override
    public List<Map<String, Object>> sumByCategoryAndMonth(String month) {
        return baseMapper.sumByCategoryAndMonth(month);
    }
}
