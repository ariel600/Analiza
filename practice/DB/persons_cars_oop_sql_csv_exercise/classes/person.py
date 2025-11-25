class Person:
    def __init__(self, person_id, name, age, email):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.email = email
        self.cars = []
    
    def add_car(self, car):
        return self.cars.append(car)
    
    def get_cars_count(self):
        return len(self.cars)
    
    def __str__(self):
        return f"person_id: {self.person_id}, name: {self.name}, age: {self.age}, email: {self.email}, cars: {self.get_cars_count()}"
        
    
    def to_dict(self):
        return {
            'person_id': self.person_id,
            'name': self.name,
            'age': self.age,
            'email': self.email,
            'cars': self.cars
        }