package com.finance.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.finance.entity.CreditCard;
import com.finance.mapper.CreditCardMapper;
import com.finance.service.CreditCardService;
import org.springframework.stereotype.Service;

@Service
public class CreditCardServiceImpl extends ServiceImpl<CreditCardMapper, CreditCard>
        implements CreditCardService {
}
