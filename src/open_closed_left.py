#!/usr/bin/env python3


class DiscountCalculator:
    def calculate_discount(self, customer_type: str, amount: float) -> float:
        if customer_type == "regular":
            return amount * 0.05
        elif customer_type == "vip":
            return amount * 0.10
        else:
            return 0


calculator = DiscountCalculator()
print(calculator.calculate_discount("regular", 100))
print(calculator.calculate_discount("vip", 100))
print(calculator.calculate_discount("new", 100))
