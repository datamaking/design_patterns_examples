from abc import ABC, abstractmethod
from typing import List

# Abstract Observer
class WeatherObserver(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass

# Concrete Observers
class WeatherDisplay(WeatherObserver):
    def __init__(self, name: str):
        self.name = name
    
    def update(self, temperature: float, humidity: float, pressure: float):
        print(f"\n{self.name} Display:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")

# Subject (Observable)
class WeatherStation:
    def __init__(self):
        self._observers: List[WeatherObserver] = []
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0
    
    def add_observer(self, observer: WeatherObserver):
        self._observers.append(observer)
    
    def remove_observer(self, observer: WeatherObserver):
        self._observers.remove(observer)
    
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)
    
    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()

# Usage example
def main():
    # Create the weather station
    weather_station = WeatherStation()
    
    # Create displays
    phone_display = WeatherDisplay("Phone")
    tablet_display = WeatherDisplay("Tablet")
    desktop_display = WeatherDisplay("Desktop")
    
    # Register displays as observers
    weather_station.add_observer(phone_display)
    weather_station.add_observer(tablet_display)
    weather_station.add_observer(desktop_display)
    
    # Simulate weather changes
    print("Weather Update 1:")
    weather_station.set_measurements(24.5, 65, 1013.2)
    
    print("\nWeather Update 2:")
    weather_station.set_measurements(27.8, 70, 1014.1)
    
    # Remove one display and update again
    weather_station.remove_observer(tablet_display)
    print("\nWeather Update 3 (after removing tablet display):")
    weather_station.set_measurements(23.4, 80, 1011.5)

if __name__ == "__main__":
    main() 