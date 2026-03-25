package com.finance.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;
import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;

@Data
@TableName("credit_card_bill")
public class CreditCardBill {
    @TableId(type = IdType.AUTO)
    private Long id;
    private Long cardId;
    private String billMonth;
    private BigDecimal billAmount;
    private BigDecimal minimumPayment;
    private Integer repaymentStatus;
    private BigDecimal actualPayment;
    private LocalDate paymentDate;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
