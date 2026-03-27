package com.finance.service;

import java.util.Map;

public interface SummaryService {

    Map<String, Object> getMonthlySummary(String month);

    Map<String, Object> getTrend();
}
