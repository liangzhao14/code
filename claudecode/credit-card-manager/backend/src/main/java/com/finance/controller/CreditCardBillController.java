package com.finance.controller;

import com.finance.dto.Result;
import com.finance.entity.CreditCardBill;
import com.finance.service.CreditCardBillService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/bills")
@RequiredArgsConstructor
public class CreditCardBillController {

    private final CreditCardBillService creditCardBillService;

    @GetMapping
    public Result<List<CreditCardBill>> list(
            @RequestParam(required = false) Long cardId,
            @RequestParam(required = false) String month) {
        if (cardId != null && month != null) {
            // 同时按卡 ID 和月份筛选
            List<CreditCardBill> bills = creditCardBillService.listByCardId(cardId);
            bills = bills.stream()
                    .filter(b -> month.equals(b.getBillMonth()))
                    .toList();
            return Result.ok(bills);
        } else if (cardId != null) {
            return Result.ok(creditCardBillService.listByCardId(cardId));
        } else if (month != null) {
            return Result.ok(creditCardBillService.listByMonth(month));
        }
        return Result.ok(creditCardBillService.list());
    }

    @GetMapping("/{id}")
    public Result<CreditCardBill> getById(@PathVariable Long id) {
        CreditCardBill bill = creditCardBillService.getById(id);
        if (bill == null) {
            return Result.error(404, "账单不存在");
        }
        return Result.ok(bill);
    }

    @PostMapping
    public Result<CreditCardBill> create(@RequestBody CreditCardBill bill) {
        creditCardBillService.save(bill);
        return Result.ok(bill);
    }

    @PutMapping("/{id}")
    public Result<CreditCardBill> update(@PathVariable Long id, @RequestBody CreditCardBill bill) {
        bill.setId(id);
        creditCardBillService.updateById(bill);
        return Result.ok(bill);
    }

    @DeleteMapping("/{id}")
    public Result<Void> delete(@PathVariable Long id) {
        creditCardBillService.removeById(id);
        return Result.ok();
    }
}
