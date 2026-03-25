package com.finance.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.finance.entity.CreditCardBill;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import java.math.BigDecimal;
import java.util.List;
import java.util.Map;

public interface CreditCardBillMapper extends BaseMapper<CreditCardBill> {

    @Select("SELECT COALESCE(SUM(actual_payment), 0) FROM credit_card_bill WHERE bill_month = #{month} AND repayment_status IN (1, 2)")
    BigDecimal sumPaymentByMonth(@Param("month") String month);

    @Select("SELECT cc.card_name, cc.bank_name, ccb.bill_amount, ccb.actual_payment, ccb.repayment_status " +
            "FROM credit_card_bill ccb JOIN credit_card cc ON ccb.card_id = cc.id " +
            "WHERE ccb.bill_month = #{month}")
    List<Map<String, Object>> getBillDetailsByMonth(@Param("month") String month);
}
