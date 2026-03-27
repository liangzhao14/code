package com.finance.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;
import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;

@Data
@TableName("expense")
public class Expense {
    @TableId(type = IdType.AUTO)
    private Long id;
    private BigDecimal amount;
    private Long categoryId;
    private LocalDate expenseDate;
    private String remark;
    private Long cardId;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
