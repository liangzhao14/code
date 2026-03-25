package com.finance.controller;

import com.finance.dto.Result;
import com.finance.service.SummaryService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.time.YearMonth;
import java.time.format.DateTimeFormatter;
import java.util.Map;

@RestController
@RequestMapping("/api/summary")
@RequiredArgsConstructor
public class SummaryController {

    private final SummaryService summaryService;

    /**
     * 月度汇总：总收入、总支出、结余、信用卡还款总额、分类统计、账单明细
     * GET /api/summary/monthly?month=YYYY-MM
     */
    @GetMapping("/monthly")
    public Result<Map<String, Object>> monthly(
            @RequestParam(required = false) String month) {
        if (month == null || month.isBlank()) {
            month = YearMonth.now().format(DateTimeFormatter.ofPattern("yyyy-MM"));
        }
        return Result.ok(summaryService.getMonthlySummary(month));
    }

    /**
     * 近6个月趋势：月份列表 + 对应收入/支出/结余数组
     * GET /api/summary/trend
     */
    @GetMapping("/trend")
    public Result<Map<String, Object>> trend() {
        return Result.ok(summaryService.getTrend());
    }
}
