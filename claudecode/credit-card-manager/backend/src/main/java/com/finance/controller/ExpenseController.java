package com.finance.controller;

import com.finance.dto.Result;
import com.finance.entity.Expense;
import com.finance.service.ExpenseService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/expenses")
@RequiredArgsConstructor
public class ExpenseController {

    private final ExpenseService expenseService;

    @GetMapping
    public Result<List<Expense>> list(
            @RequestParam(required = false) Long categoryId,
            @RequestParam(required = false) String month) {
        if (month != null) {
            // listByCategoryAndMonth 内部处理 categoryId 为 null 的情况
            return Result.ok(expenseService.listByCategoryAndMonth(categoryId, month));
        } else if (categoryId != null) {
            return Result.ok(expenseService.listByCategoryId(categoryId));
        }
        return Result.ok(expenseService.list());
    }

    @GetMapping("/{id}")
    public Result<Expense> getById(@PathVariable Long id) {
        Expense expense = expenseService.getById(id);
        if (expense == null) {
            return Result.error(404, "支出记录不存在");
        }
        return Result.ok(expense);
    }

    @PostMapping
    public Result<Expense> create(@RequestBody Expense expense) {
        expenseService.save(expense);
        return Result.ok(expense);
    }

    @PutMapping("/{id}")
    public Result<Expense> update(@PathVariable Long id, @RequestBody Expense expense) {
        expense.setId(id);
        expenseService.updateById(expense);
        return Result.ok(expense);
    }

    @DeleteMapping("/{id}")
    public Result<Void> delete(@PathVariable Long id) {
        expenseService.removeById(id);
        return Result.ok();
    }
}
