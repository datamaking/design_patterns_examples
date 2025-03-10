from abc import ABC, abstractmethod

# Abstract Products
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

class Table(ABC):
    @abstractmethod
    def place_item(self, item):
        pass

class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass

# Modern Furniture Products
class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a sleek modern chair"

class ModernTable(Table):
    def place_item(self, item):
        return f"Placing {item} on a minimalist modern table"

class ModernSofa(Sofa):
    def lie_on(self):
        return "Lying on a modern L-shaped sofa"

# Victorian Furniture Products
class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on an ornate Victorian chair"

class VictorianTable(Table):
    def place_item(self, item):
        return f"Placing {item} on an antique Victorian table"

class VictorianSofa(Sofa):
    def lie_on(self):
        return "Lying on a luxurious Victorian sofa"

# Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass
    
    @abstractmethod
    def create_table(self) -> Table:
        pass
    
    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

# Concrete Factories
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()
    
    def create_table(self) -> Table:
        return ModernTable()
    
    def create_sofa(self) -> Sofa:
        return ModernSofa()

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()
    
    def create_table(self) -> Table:
        return VictorianTable()
    
    def create_sofa(self) -> Sofa:
        return VictorianSofa()

# Client code
def create_furniture_set(factory: FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()
    sofa = factory.create_sofa()
    
    print(chair.sit_on())
    print(table.place_item("coffee cup"))
    print(sofa.lie_on())

def main():
    print("Creating Modern Furniture Set:")
    create_furniture_set(ModernFurnitureFactory())
    
    print("\nCreating Victorian Furniture Set:")
    create_furniture_set(VictorianFurnitureFactory())

if __name__ == "__main__":
    main() 