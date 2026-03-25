package com.finance.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.finance.entity.Expense;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import java.math.BigDecimal;
import java.util.List;
import java.util.Map;

public interface ExpenseMapper extends BaseMapper<Expense> {

    @Select("SELECT COALESCE(SUM(amount), 0) FROM expense WHERE DATE_FORMAT(expense_date, '%Y-%m') = #{month}")
    BigDecimal sumByMonth(@Param("month") String month);

    @Select("SELECT ec.name AS category_name, COALESCE(SUM(e.amount), 0) AS total " +
            "FROM expense e JOIN expense_category ec ON e.category_id = ec.id " +
            "WHERE DATE_FORMAT(e.expense_date, '%Y-%m') = #{month} " +
            "GROUP BY ec.name ORDER BY total DESC")
    List<Map<String, Object>> sumByCategoryAndMonth(@Param("month") String month);
}
