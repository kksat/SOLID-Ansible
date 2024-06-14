#!/usr/bin/env python3

from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, amount: float) -> float:
        pass


class RegularCustomerDiscount(DiscountStrategy):
    def calculate_discount(self, amount: float) -> float:
        return amount * 0.05


class VIPCustomerDiscount(DiscountStrategy):
    def calculate_discount(self, amount: float) -> float:
        return amount * 0.10


class DiscountCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate_discount(self, amount: float) -> float:
        return self.strategy.calculate_discount(amount)


regular_discount = RegularCustomerDiscount()
vip_discount = VIPCustomerDiscount()

calculator_regular = DiscountCalculator(regular_discount)
calculator_vip = DiscountCalculator(vip_discount)

print(calculator_regular.calculate_discount(100))
print(calculator_vip.calculate_discount(100))
