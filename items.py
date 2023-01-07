# Base class for all items
class Item():

    def __init__(self, name, description, value):
        self.name = name  # attribute of the Item class and any subclasses
        self.description = description  # attribute of the Item class and any subclasses
        self.value = value  # attribute of the Item class and any subclasses

    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


# Extend the Items class
# Gold class will be a child or subclass of the superclass Item
class Gold(Item):
    # __init__ is the contructor method
    def __init__(self, amt):
        self.amt = amt  # attribute of the Gold class
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=1,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=20,
                         damage=10)


class RustySword(Weapon):
    def __init__(self):
        super().__init__(name="Rusty Sword",
                         description="This sword is showing its age, but still has some fight in it",
                         value=20,
                         damage=50)

class Consumable(Item):
    def __init__(self, name, healing_value, value):
        self.healing_value = healing_value
        super().__init__(name, healing_value, value)

    def __str__(self):
        return "{}\n=====\nHealing Value: {}\nValue: {}".format(self.name, self.description, self.healing_value, self.value)

class FreshBread(Consumable):
    def __init__(self):
        super().__init__(name="Fresh Bread",
                         healing_value=10,
                         value=12)

class HealingPotion(Consumable):
    def __init__(self):
        super().__init__(name="Healing Potion",
                         healing_value=50,
                         value=60)

class Mazeltov(Weapon):
    def __init__(self):
        super().__init__(name="Mazeltov",
                         description="A mazeltov to burn your enemies.",
                         value=200,
                         damage=80)

class Crossbow(Weapon):
    def __init__(self):
        super().__init__(name="Crossbow",
                         description="A crossbow to put holes in the enemies. ",
                         value=100,
                         damage=45)
