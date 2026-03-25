package com.finance.controller;

import com.finance.dto.Result;
import com.finance.entity.Income;
import com.finance.service.IncomeService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/incomes")
@RequiredArgsConstructor
public class IncomeController {

    private final IncomeService incomeService;

    @GetMapping
    public Result<List<Income>> list(@RequestParam(required = false) String month) {
        if (month != null) {
            return Result.ok(incomeService.listByMonth(month));
        }
        return Result.ok(incomeService.list());
    }

    @GetMapping("/{id}")
    public Result<Income> getById(@PathVariable Long id) {
        Income income = incomeService.getById(id);
        if (income == null) {
            return Result.error(404, "收入记录不存在");
        }
        return Result.ok(income);
    }

    @PostMapping
    public Result<Income> create(@RequestBody Income income) {
        incomeService.save(income);
        return Result.ok(income);
    }

    @PutMapping("/{id}")
    public Result<Income> update(@PathVariable Long id, @RequestBody Income income) {
        income.setId(id);
        incomeService.updateById(income);
        return Result.ok(income);
    }

    @DeleteMapping("/{id}")
    public Result<Void> delete(@PathVariable Long id) {
        incomeService.removeById(id);
        return Result.ok();
    }
}
