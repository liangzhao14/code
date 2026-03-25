-- 信用卡还款与收支管理系统 - 数据库初始化脚本
CREATE DATABASE IF NOT EXISTS finance_manager DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE finance_manager;

-- 用户表（单用户）
CREATE TABLE IF NOT EXISTS `user` (
    `id` BIGINT PRIMARY KEY AUTO_INCREMENT,
    `username` VARCHAR(50) NOT NULL UNIQUE,
    `password` VARCHAR(255) NOT NULL,
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 信用卡信息表
CREATE TABLE IF NOT EXISTS `credit_card` (
    `id` BIGINT PRIMARY KEY AUTO_INCREMENT,
    `card_name` VARCHAR(100) NOT NULL COMMENT '卡名称，如招行金卡',
    `bank_name` VARCHAR(100) NOT NULL COMMENT '银行名称',
    `card_last_four` VARCHAR(4) NOT NULL COMMENT '卡号后四位',
    `billing_day` INT NOT NULL COMMENT '账单日（每月几号）',
    `due_day` INT NOT NULL COMMENT '还款日（每月几号）',
    `credit_limit` DECIMAL(12,2) DEFAULT 0 COMMENT '信用额度',
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 信用卡月度账单表
CREATE TABLE IF NOT EXISTS `credit_card_bill` (
    `id` BIGINT PRIMARY KEY AUTO_INCREMENT,
    `card_id` BIGINT NOT NULL COMMENT '关联信用卡ID',
    `bill_month` VARCHAR(7) NOT NULL COMMENT '账单月份，格式 YYYY-MM',
    `bill_amount` DECIMAL(12,2) NOT NULL COMMENT '账单金额',
    `minimum_payment` DECIMAL(12,2) DEFAULT NULL COMMENT '最低还款额',
    `repayment_status` TINYINT NOT NULL DEFAULT 0 COMMENT '还款状态：0-未还 1-已还 2-部分还款',
    `actual_payment` DECIMAL(12,2) DEFAULT NULL COMMENT '实际还款金额',
    `payment_date` DATE DEFAULT NULL COMMENT '还款日期',
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (`card_id`) REFERENCES `credit_card`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 收入记录表
CREATE TABLE IF NOT EXISTS `income` (
    `id` BIGINT PRIMARY KEY AUTO_INCREMENT,
    `amount` DECIMAL(12,2) NOT NULL COMMENT '金额',
    `income_type` VARCHAR(50) NOT NULL COMMENT '收入类型：工资/奖金/其他',
    `income_date` DATE NOT NULL COMMENT '收入日期',
    `remark` VARCHAR(255) DEFAULT NULL COMMENT '备注',
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 支出分类表
CREATE TABLE IF NOT EXISTS `expense_category` (
    `id` BIGINT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL UNIQUE COMMENT '分类名称',
    `sort_order` INT DEFAULT 0 COMMENT '排序',
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 支出记录表
CREATE TABLE IF NOT EXISTS `expense` (
    `id` BIGINT PRIMARY KEY AUTO_INCREMENT,
    `amount` DECIMAL(12,2) NOT NULL COMMENT '金额',
    `category_id` BIGINT NOT NULL COMMENT '支出分类ID',
    `expense_date` DATE NOT NULL COMMENT '支出日期',
    `remark` VARCHAR(255) DEFAULT NULL COMMENT '备注',
    `card_id` BIGINT DEFAULT NULL COMMENT '关联信用卡ID（可选）',
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (`category_id`) REFERENCES `expense_category`(`id`),
    FOREIGN KEY (`card_id`) REFERENCES `credit_card`(`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 插入默认支出分类
INSERT INTO `expense_category` (`name`, `sort_order`) VALUES
('餐饮', 1),
('交通', 2),
('购物', 3),
('房贷房租', 4),
('水电燃气', 5),
('娱乐', 6),
('医疗', 7),
('教育', 8),
('其他', 9);

-- 默认管理员账号通过 POST /api/auth/init 接口创建
-- 首次启动后访问该接口设置用户名和密码，例如：
-- curl -X POST http://localhost:8081/api/auth/init -H "Content-Type: application/json" -d '{"username":"admin","password":"admin123"}'
