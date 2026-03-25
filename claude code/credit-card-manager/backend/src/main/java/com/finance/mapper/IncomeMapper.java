package com.finance.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.finance.entity.Income;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import java.math.BigDecimal;

public interface IncomeMapper extends BaseMapper<Income> {

    @Select("SELECT COALESCE(SUM(amount), 0) FROM income WHERE DATE_FORMAT(income_date, '%Y-%m') = #{month}")
    BigDecimal sumByMonth(@Param("month") String month);
}
