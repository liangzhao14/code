package com.finance.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.finance.entity.Expense;

import java.math.BigDecimal;
import java.util.List;
import java.util.Map;

public interface ExpenseService extends IService<Expense> {

    List<Expense> listByMonth(String month);

    List<Expense> listByCategoryId(Long categoryId);

    List<Expense> listByCategoryAndMonth(Long categoryId, String month);

    BigDecimal sumByMonth(String month);

    List<Map<String, Object>> sumByCategoryAndMonth(String month);
}
