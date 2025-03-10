from abc import ABC, abstractmethod

# Abstract Payment Processor
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Concrete Payment Processors
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")
        return f"Credit card payment of ${amount} processed"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")
        return f"PayPal payment of ${amount} processed"

class CryptoProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing cryptocurrency payment of ${amount}")
        return f"Crypto payment of ${amount} processed"

# Payment Processor Factory
class PaymentProcessorFactory:
    @staticmethod
    def create_processor(payment_method):
        if payment_method.lower() == "credit":
            return CreditCardProcessor()
        elif payment_method.lower() == "paypal":
            return PayPalProcessor()
        elif payment_method.lower() == "crypto":
            return CryptoProcessor()
        else:
            raise ValueError("Invalid payment method")

# Usage example
def main():
    factory = PaymentProcessorFactory()
    
    # Process different types of payments
    payment_methods = ["credit", "paypal", "crypto"]
    amount = 100.00
    
    for method in payment_methods:
        processor = factory.create_processor(method)
        result = processor.process_payment(amount)
        print(f"Result: {result}\n")

if __name__ == "__main__":
    main() 