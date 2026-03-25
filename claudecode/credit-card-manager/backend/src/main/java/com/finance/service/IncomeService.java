package com.finance.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.finance.entity.Income;

import java.math.BigDecimal;
import java.util.List;

public interface IncomeService extends IService<Income> {

    List<Income> listByMonth(String month);

    BigDecimal sumByMonth(String month);
}
