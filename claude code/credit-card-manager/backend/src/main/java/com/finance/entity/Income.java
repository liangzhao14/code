package com.finance.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;
import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;

@Data
@TableName("income")
public class Income {
    @TableId(type = IdType.AUTO)
    private Long id;
    private BigDecimal amount;
    private String incomeType;
    private LocalDate incomeDate;
    private String remark;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
