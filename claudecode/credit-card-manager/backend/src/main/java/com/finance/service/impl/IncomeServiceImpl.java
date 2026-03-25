package com.finance.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.finance.entity.Income;
import com.finance.mapper.IncomeMapper;
import com.finance.service.IncomeService;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.time.YearMonth;
import java.time.format.DateTimeFormatter;
import java.util.List;

@Service
public class IncomeServiceImpl extends ServiceImpl<IncomeMapper, Income>
        implements IncomeService {

    @Override
    public List<Income> listByMonth(String month) {
        YearMonth ym = YearMonth.parse(month, DateTimeFormatter.ofPattern("yyyy-MM"));
        return list(new LambdaQueryWrapper<Income>()
                .ge(Income::getIncomeDate, ym.atDay(1))
                .le(Income::getIncomeDate, ym.atEndOfMonth())
                .orderByDesc(Income::getIncomeDate));
    }

    @Override
    public BigDecimal sumByMonth(String month) {
        return baseMapper.sumByMonth(month);
    }
}
