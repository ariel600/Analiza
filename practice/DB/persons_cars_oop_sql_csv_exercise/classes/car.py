from datetime import datetime

class Car:
    def __init__(self, car_id, brand, model, year, color, owner_id=None):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.owner_id = owner_id
    
    def get_age(self):
        year = datetime.now().year
        return year - self.year
    
    def __str__(self):
        return f"car_id: {self.car_id}, brand: {self.brand}, model: {self.model}, year: {self.year}, color: {self.color(), "owner_id": {self.owner_id}}"
    
    def to_dict(self):
        return {
            "car_id": self.car_id,
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "color": self.color,
            "owner_id": self.owner_id
        }
