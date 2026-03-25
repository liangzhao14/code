package com.finance.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Data
@TableName("credit_card")
public class CreditCard {
    @TableId(type = IdType.AUTO)
    private Long id;
    private String cardName;
    private String bankName;
    private String cardLastFour;
    private Integer billingDay;
    private Integer dueDay;
    private BigDecimal creditLimit;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
