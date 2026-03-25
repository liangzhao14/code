package com.finance.controller;

import com.finance.dto.Result;
import com.finance.entity.CreditCard;
import com.finance.service.CreditCardService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/cards")
@RequiredArgsConstructor
public class CreditCardController {

    private final CreditCardService creditCardService;

    @GetMapping
    public Result<List<CreditCard>> list() {
        return Result.ok(creditCardService.list());
    }

    @GetMapping("/{id}")
    public Result<CreditCard> getById(@PathVariable Long id) {
        CreditCard card = creditCardService.getById(id);
        if (card == null) {
            return Result.error(404, "信用卡不存在");
        }
        return Result.ok(card);
    }

    @PostMapping
    public Result<CreditCard> create(@RequestBody CreditCard creditCard) {
        creditCardService.save(creditCard);
        return Result.ok(creditCard);
    }

    @PutMapping("/{id}")
    public Result<CreditCard> update(@PathVariable Long id, @RequestBody CreditCard creditCard) {
        creditCard.setId(id);
        creditCardService.updateById(creditCard);
        return Result.ok(creditCard);
    }

    @DeleteMapping("/{id}")
    public Result<Void> delete(@PathVariable Long id) {
        creditCardService.removeById(id);
        return Result.ok();
    }
}
