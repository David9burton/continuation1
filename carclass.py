class Car:
    def __init__(self):
        self.brand = input("Enter the brand of the car: ")
        self.model = input("Enter the model of the car: ")
        self.year = input("Enter the year of the car: ")

    def display_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"
        
    def honk(self):
        return "Honk! Honk!"
    
car1 = Car()
print(car1.display_details())
print(car1.honk())

class ElectricCar(Car):
    def __init__(self):
        super().__init__()
        self.battery_capacity = input("Enter the battery capacity (kWh): ")

    def display_battery_status(self):
        return f"Battery Capacity: {self.battery_capacity} kWh"

e_car = ElectricCar()
print(e_car.display_details())
print(e_car.display_battery_status())


