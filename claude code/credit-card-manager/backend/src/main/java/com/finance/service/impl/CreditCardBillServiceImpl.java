package com.finance.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.finance.entity.CreditCardBill;
import com.finance.mapper.CreditCardBillMapper;
import com.finance.service.CreditCardBillService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.util.List;
import java.util.Map;

@Service
@RequiredArgsConstructor
public class CreditCardBillServiceImpl extends ServiceImpl<CreditCardBillMapper, CreditCardBill>
        implements CreditCardBillService {

    @Override
    public List<CreditCardBill> listByCardId(Long cardId) {
        return list(new LambdaQueryWrapper<CreditCardBill>()
                .eq(CreditCardBill::getCardId, cardId)
                .orderByDesc(CreditCardBill::getBillMonth));
    }

    @Override
    public List<CreditCardBill> listByMonth(String month) {
        return list(new LambdaQueryWrapper<CreditCardBill>()
                .eq(CreditCardBill::getBillMonth, month));
    }

    @Override
    public BigDecimal sumPaymentByMonth(String month) {
        return baseMapper.sumPaymentByMonth(month);
    }

    @Override
    public List<Map<String, Object>> getBillDetailsByMonth(String month) {
        return baseMapper.getBillDetailsByMonth(month);
    }
}
