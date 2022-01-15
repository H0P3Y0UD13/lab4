import random


heroes = {}


class Heroes:

    def __init__(self, name):
        self.name = name
    
    def __add__(self, other):
        return other + self.name

    def show_data(self):
        print("Hi, my name is " + self.name)

    def use_random_spell(self):
        print(self.name + " just used...", end = "")


class Int_heroes(Heroes):

    def __init__(self, atribute, name, damage, spells):
        super().__init__(name)
        self.damage = damage
        self.spells = str(spells).split(", ")
        self.atribute = atribute

    def show_data(self):
        super().show_data()
        print("I have skills:", ', '.join(self.spells))
        print("I have " + str(self.damage), " damage points.")
        print("My atribute is " + str(self.atribute) + ". My power is in magic.")

    def use_spell(self):
        super().use_random_spell()
        print(self.spells[random.randrange(0,3)], "\n")


class Str_heroes(Heroes):

    def __init__(self, atribute, name, damage, spells):
        super().__init__(name)
        self.damage = damage
        self.spells = str(spells).split(", ")
        self.atribute = atribute

    def show_data(self):
        super().show_data()
        print("I have skills:", ', '.join(self.spells))
        print("I have " + str(self.damage), " damage points.")
        print("My atribute is " + str(self.atribute) + ". My power is in physical damage.")

    def use_spell(self):
        super().use_random_spell()
        print(self.spells[random.randrange(0,3)], "\n")


class Agl_heroes(Heroes):

    def __init__(self, atribute, name, damage, spells):
        super().__init__(name)
        self.damage = damage
        self.spells = str(spells).split(", ")
        self.atribute = atribute

    def show_data(self):
        super().show_data()
        print("I have skills:", ', '.join(self.spells))
        print(str(self.spells).strip('[]'))
        print("I have " + str(self.damage), " damage points.")
        print("My atribute is " + str(self.atribute) + ". My power is in attack and running speed.")

    def use_spell(self):
        super().use_random_spell()
        print(self.spells[random.randrange(0,3)], "\n")


class Gods(Int_heroes):

    def __init__(self, atribute, name, damage, spells, ultra_spell):
        super().__init__(atribute, name, damage, spells)
        self.ultra_spell = ultra_spell

    def show_the_divine(self):
        print("So, I am god of this world. Behold my divine punishment! ", self.ultra_spell)