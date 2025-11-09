# Exercise 1
class Weapon:
    total_weapons = 0
    def __init__(self, name: str, ammo: int):
        self.name = name
        self.ammo = ammo
        Weapon.total_weapons += 1

class Soldier:
    def __init__(self, name: str, rank: str, weapon: Weapon):
        self.name = name
        self.rank = rank
        self.weapon = weapon
    
    def report(self):
        print(f"name: {self.name}, rank: {self.rank}, weapon: {self.weapon.name}, {self.weapon.ammo}.")

class Unit:
    def __init__(self, unit_name: str, commander: Soldier, soldiers: list[Soldier], strike_option):
        self.unit_name = unit_name
        self.commander = commander
        self.soldiers = soldiers
        self.strike_option = strike_option
    
    def briefing(self):
        print(f"unit name: {self.unit_name}, commander: {self.commander}.")

# Exercise 2
class StrikeOption:
    def __init__(self, name: str, ammo: int):
        self.name = name
        self.ammo = ammo
    
    def strike(self):
        pass

class Tank(StrikeOption):
    def __init__(self, name, ammo):
        super().__init__(name, ammo)
    
    def strike(self):
        print("Tank")

class Drone(StrikeOption):
    def __init__(self, name, ammo):
        super().__init__(name, ammo)

    def strike(self):
        print("Drone")

# Exercise 5
class Army:
    total_attacks = 0
    def __init__(self, units: list[Unit]):
        self.units = units
    
    def attack_all(self):
        for unit in self.units:
            unit.strike_option.strike()
            Army.total_attacks += 1
            