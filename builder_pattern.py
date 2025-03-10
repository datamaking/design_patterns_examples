from abc import ABC, abstractmethod
from typing import Any

class Computer:
    def __init__(self):
        self.parts = {}
    
    def add_part(self, key: str, value: Any):
        self.parts[key] = value
    
    def show_specs(self):
        print("\nComputer Specifications:")
        for key, value in self.parts.items():
            print(f"{key}: {value}")

class ComputerBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def build_processor(self):
        pass
    
    @abstractmethod
    def build_memory(self):
        pass
    
    @abstractmethod
    def build_storage(self):
        pass
    
    @abstractmethod
    def build_graphics(self):
        pass
    
    @abstractmethod
    def get_result(self) -> Computer:
        pass

class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._computer = Computer()
    
    def build_processor(self):
        self._computer.add_part("Processor", "Intel Core i9-12900K")
    
    def build_memory(self):
        self._computer.add_part("Memory", "32GB DDR5 RAM")
    
    def build_storage(self):
        self._computer.add_part("Storage", "2TB NVMe SSD")
    
    def build_graphics(self):
        self._computer.add_part("Graphics", "NVIDIA RTX 4090")
    
    def get_result(self) -> Computer:
        computer = self._computer
        self.reset()
        return computer

class OfficeComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._computer = Computer()
    
    def build_processor(self):
        self._computer.add_part("Processor", "Intel Core i5-12400")
    
    def build_memory(self):
        self._computer.add_part("Memory", "16GB DDR4 RAM")
    
    def build_storage(self):
        self._computer.add_part("Storage", "512GB SSD")
    
    def build_graphics(self):
        self._computer.add_part("Graphics", "Intel UHD Graphics")
    
    def get_result(self) -> Computer:
        computer = self._computer
        self.reset()
        return computer

class ComputerAssembler:
    def __init__(self, builder: ComputerBuilder):
        self._builder = builder
    
    def construct_computer(self):
        self._builder.build_processor()
        self._builder.build_memory()
        self._builder.build_storage()
        self._builder.build_graphics()
    
    def get_computer(self) -> Computer:
        return self._builder.get_result()

def main():
    # Create a gaming computer
    gaming_builder = GamingComputerBuilder()
    assembler = ComputerAssembler(gaming_builder)
    
    print("Building a gaming computer...")
    assembler.construct_computer()
    gaming_computer = assembler.get_computer()
    gaming_computer.show_specs()
    
    # Create an office computer
    office_builder = OfficeComputerBuilder()
    assembler = ComputerAssembler(office_builder)
    
    print("\nBuilding an office computer...")
    assembler.construct_computer()
    office_computer = assembler.get_computer()
    office_computer.show_specs()

if __name__ == "__main__":
    main() 