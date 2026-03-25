package com.finance.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.finance.dto.Result;
import com.finance.entity.ExpenseCategory;
import com.finance.service.ExpenseCategoryService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/categories")
@RequiredArgsConstructor
public class ExpenseCategoryController {

    private final ExpenseCategoryService expenseCategoryService;

    @GetMapping
    public Result<List<ExpenseCategory>> list() {
        List<ExpenseCategory> categories = expenseCategoryService.list(
                new LambdaQueryWrapper<ExpenseCategory>().orderByAsc(ExpenseCategory::getSortOrder));
        return Result.ok(categories);
    }

    @GetMapping("/{id}")
    public Result<ExpenseCategory> getById(@PathVariable Long id) {
        ExpenseCategory category = expenseCategoryService.getById(id);
        if (category == null) {
            return Result.error(404, "分类不存在");
        }
        return Result.ok(category);
    }

    @PostMapping
    public Result<ExpenseCategory> create(@RequestBody ExpenseCategory category) {
        expenseCategoryService.save(category);
        return Result.ok(category);
    }

    @PutMapping("/{id}")
    public Result<ExpenseCategory> update(@PathVariable Long id, @RequestBody ExpenseCategory category) {
        category.setId(id);
        expenseCategoryService.updateById(category);
        return Result.ok(category);
    }

    @DeleteMapping("/{id}")
    public Result<Void> delete(@PathVariable Long id) {
        expenseCategoryService.removeById(id);
        return Result.ok();
    }
}
