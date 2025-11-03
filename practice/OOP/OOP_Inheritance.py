class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("The vehicle is moving")
        
class Car(Vehicle):
    def move(self):
        print("The car drives")

class Plane(Vehicle):
    def move(self):
        print("The plane flies")
      
v = Vehicle("ford", "explorer")
c = Car("toyota", "siena")
p = Plane("boing", "747")
l = [v, c, p]
for i in l:
    i.move()    


class Animals:
    def __init__(self, name):
        self.name = name
        
    def sound(self):
        pass
    
class Dog(Animals):
    def sound(self):
        return "Woof"
    
class Cat(Animals):
    def sound(self):
        return "Meow"

# a = Animals("tiger")
# d = Dog("noga")
# c = Cat("shhori")
# l = [a, d, c]
# for i in l:
#     print(i.sound())