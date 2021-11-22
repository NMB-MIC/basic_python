class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odomoter(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self,miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        print("This car need a gas tank!")

class Battery:
    def __init__(self,battery_size=75):
        self.battery_size = battery_size

    def describe_batterry(self):
        print(f"This car has a {self.battery_size}-kwh battery.")
    
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

#Inheritance
class ElectricCar(Car):
    def __init__(self,make,model,year,battery_size):
        super().__init__(make,model,year)
        self.battery = Battery(battery_size)
       
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', '2021',battery_size=100)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_batterry()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()
# my_new_car = Car('audi','a4',2021)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odomoter()

# # my_new_car.odometer_reading = 23
# # my_new_car.read_odomoter()

# my_new_car.update_odometer(-6)
# my_new_car.read_odomoter()

# my_new_car.update_odometer(20)
# my_new_car.read_odomoter()

# my_new_car.increment_odometer(100)
# my_new_car.read_odomoter()