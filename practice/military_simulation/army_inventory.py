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
        print(f"name: {self.name}, rank: {self.rank}, weapon: {self.weapon}.")

class Unit:
    def __init__(self, unit_name: str, commander: Soldier, soldiers: list[Soldier]):
        self.unit_name = unit_name
        self.commander = commander
        self.soldiers = soldiers
    
    def briefing(self):
        print(f"unit name: {self.unit_name}, commander: {self.commander}.")
