package com.finance.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.finance.entity.ExpenseCategory;
import com.finance.mapper.ExpenseCategoryMapper;
import com.finance.service.ExpenseCategoryService;
import org.springframework.stereotype.Service;

@Service
public class ExpenseCategoryServiceImpl extends ServiceImpl<ExpenseCategoryMapper, ExpenseCategory>
        implements ExpenseCategoryService {
}
