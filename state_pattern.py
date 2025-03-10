from abc import ABC, abstractmethod
from typing import Dict

class VendingMachineState(ABC):
    @abstractmethod
    def insert_money(self, amount: float) -> str:
        pass
    
    @abstractmethod
    def select_product(self, product: str) -> str:
        pass
    
    @abstractmethod
    def dispense_product(self) -> str:
        pass
    
    @abstractmethod
    def refund(self) -> str:
        pass

class VendingMachine:
    def __init__(self):
        self.no_money_state = NoMoneyState(self)
        self.has_money_state = HasMoneyState(self)
        self.dispensing_state = DispensingState(self)
        
        self._state = self.no_money_state
        self.amount = 0.0
        self.products: Dict[str, float] = {
            "cola": 2.00,
            "chips": 1.50,
            "candy": 1.00
        }
        self.selected_product = None
    
    def insert_money(self, amount: float) -> str:
        return self._state.insert_money(amount)
    
    def select_product(self, product: str) -> str:
        return self._state.select_product(product)
    
    def dispense_product(self) -> str:
        return self._state.dispense_product()
    
    def refund(self) -> str:
        return self._state.refund()
    
    def set_state(self, state: VendingMachineState):
        self._state = state

class NoMoneyState(VendingMachineState):
    def __init__(self, machine: VendingMachine):
        self.machine = machine
    
    def insert_money(self, amount: float) -> str:
        self.machine.amount += amount
        self.machine.set_state(self.machine.has_money_state)
        return f"${amount:.2f} inserted. Total: ${self.machine.amount:.2f}"
    
    def select_product(self, product: str) -> str:
        return "Please insert money first"
    
    def dispense_product(self) -> str:
        return "Please insert money first"
    
    def refund(self) -> str:
        return "No money to refund"

class HasMoneyState(VendingMachineState):
    def __init__(self, machine: VendingMachine):
        self.machine = machine
    
    def insert_money(self, amount: float) -> str:
        self.machine.amount += amount
        return f"${amount:.2f} inserted. Total: ${self.machine.amount:.2f}"
    
    def select_product(self, product: str) -> str:
        if product not in self.machine.products:
            return f"Invalid product: {product}"
        
        price = self.machine.products[product]
        if self.machine.amount >= price:
            self.machine.selected_product = product
            self.machine.set_state(self.machine.dispensing_state)
            return f"Selected {product}. Price: ${price:.2f}"
        else:
            return f"Insufficient funds. Need ${price - self.machine.amount:.2f} more"
    
    def dispense_product(self) -> str:
        return "Please select a product first"
    
    def refund(self) -> str:
        amount = self.machine.amount
        self.machine.amount = 0.0
        self.machine.set_state(self.machine.no_money_state)
        return f"Refunded ${amount:.2f}"

class DispensingState(VendingMachineState):
    def __init__(self, machine: VendingMachine):
        self.machine = machine
    
    def insert_money(self, amount: float) -> str:
        return "Please wait, dispensing product"
    
    def select_product(self, product: str) -> str:
        return "Please wait, dispensing product"
    
    def dispense_product(self) -> str:
        product = self.machine.selected_product
        price = self.machine.products[product]
        change = self.machine.amount - price
        self.machine.amount = 0.0
        self.machine.selected_product = None
        self.machine.set_state(self.machine.no_money_state)
        
        result = f"Dispensing {product}"
        if change > 0:
            result += f"\nReturning change: ${change:.2f}"
        return result
    
    def refund(self) -> str:
        return "Cannot refund during dispensing"

def main():
    # Create a vending machine
    machine = VendingMachine()
    
    # Test the vending machine
    print("1.", machine.select_product("cola"))  # Should fail - no money
    print("2.", machine.insert_money(1.00))
    print("3.", machine.insert_money(0.50))
    print("4.", machine.select_product("cola"))  # Should fail - not enough money
    print("5.", machine.insert_money(1.00))
    print("6.", machine.select_product("cola"))  # Should succeed
    print("7.", machine.dispense_product())
    
    print("\nNew transaction:")
    print("8.", machine.insert_money(5.00))
    print("9.", machine.select_product("chips"))
    print("10.", machine.dispense_product())

if __name__ == "__main__":
    main() 