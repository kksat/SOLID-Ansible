#!/usr/bin/env python3

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing payment of ${amount} through PayPal.")


class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing payment of ${amount} through Stripe.")


class PaymentService:
    def __init__(self, processor: PaymentProcessor):
        self.processor = processor

    def make_payment(self, amount: float):
        self.processor.process_payment(amount)


paypal_processor = PayPalProcessor()
stripe_processor = StripeProcessor()

payment_service = PaymentService(paypal_processor)
payment_service.make_payment(100.0)

payment_service = PaymentService(stripe_processor)
payment_service.make_payment(200.0)
