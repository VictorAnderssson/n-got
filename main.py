import random 

class Player:
    def __init__(self, hp, strength, lvl, inventory=[]):
        self.hp = hp
        self.strength = strength
        self.inventory = inventory
        self.lvl = lvl

    def change_hp(self, val):
        self.hp += val

    def open_inventory(self):
        sel = input(f"select item or press q to close inventory: {[i.name for i in self.inventory]}")
        if sel != "q":
            self.use_item(sel)

    def use_item(self, sel):
        self.inventory[sel + 1]


    def show_inventory(self):
        for i in self.inventory:
            print(f"name: {i.name} strength bonus: {i.strength_bonus}")

class Monster:
    def __init__(self) -> None:
        self.name = random.choice(["Skeleton", "Zombie", "Goblin"])
        self.strength = random.randint(15,30)


class Item:
    def __init__(self, name, strength_bonus, hp_bonus):
        self.name = name
        self.strength_bonus = strength_bonus
        self.hp_bonus = hp_bonus


