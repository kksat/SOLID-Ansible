class PayPalProcessor:
    def process_payment(self, amount: float):
        print(f"Processing payment of ${amount} through PayPal.")


class StripeProcessor:
    def process_payment(self, amount: float):
        print(f"Processing payment of ${amount} through Stripe.")


class PaymentService:
    def __init__(self, processor_type: str):
        if processor_type == "paypal":
            self.processor = PayPalProcessor()
        elif processor_type == "stripe":
            self.processor = StripeProcessor()
        else:
            raise ValueError("Unknown processor type")

    def make_payment(self, amount: float):
        self.processor.process_payment(amount)


payment_service = PaymentService("paypal")
payment_service.make_payment(100.0)

payment_service = PaymentService("stripe")
payment_service.make_payment(200.0)
