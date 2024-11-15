""""""
### PRACTICE

#1. **Car Class Implementation:** Create a `Car` class with methods like `start_engine`.
#2. **Electric Car Extension:** Develop an `ElectricCar` subclass with unique attributes.
#3. **Polymorphism Demonstration:** Use method overriding to demonstrate polymorphism with animal classes.

""""""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.engine_on = False

    def start_engine(self):
        print(f"The {self.model}'s engine is started.")
        self.engine_on = True

    def stop_engine(self):
        print(f"The {self.model}'s engine is stopped.")
        self.engine_on = False
    def check_engine_status(self):
        print(f"The {self.model}'s engine is {'running' if self.engine_on else 'Off'}.")
car = Car("Ford", "Mustang", 2012)

car.check_engine_status()
car.start_engine()
car.check_engine_status()
car.stop_engine()
car.check_engine_status()

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def start_engine(self):
        print(f"The {self.model}'s electric motor is started with a {self.battery_size}-kWh battery.")

    def charge_battery(self):
        print(f"The {self.model}'s battery is charging.")

    def drive(self):
        print(f"The {self.model} is driving on electric power.")
        self.battery_size -= 10
        self.battery_size = 100

tesla = ElectricCar("Tesla", "Model 3", 2022, 100)

tesla.start_engine()
tesla.check_engine_status()
tesla.charge_battery()
tesla.check_engine_status()
tesla.drive()
tesla.check_engine_status()
