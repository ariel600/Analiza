class Vehicle:
    def __init__(self, max_speed: int):
        self.max_speed = max_speed

    def drive(self):
        print(self.max_speed)

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary    

class Manager(Employee):
    def manage():
        print("manage")

class Developer(Employee):
    def write_code():
        print("write_code")