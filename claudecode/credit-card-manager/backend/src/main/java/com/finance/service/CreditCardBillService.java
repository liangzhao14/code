package com.finance.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.finance.entity.CreditCardBill;

import java.math.BigDecimal;
import java.util.List;
import java.util.Map;

public interface CreditCardBillService extends IService<CreditCardBill> {

    List<CreditCardBill> listByCardId(Long cardId);

    List<CreditCardBill> listByMonth(String month);

    BigDecimal sumPaymentByMonth(String month);

    List<Map<String, Object>> getBillDetailsByMonth(String month);
}
