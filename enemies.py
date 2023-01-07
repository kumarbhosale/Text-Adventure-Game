class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2)
 
class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=10)

class BatColony(Enemy):
    def __init__(self):
        super().__init__(name="Colony of Bats", hp=100, damage=4)

class Wolf(Enemy):
    def __init__(self):
        super().__init__(name="Wolf", hp=25, damage=15)

class RockMonster(Enemy):
    def __init__(self):
        super().__init__(name="Rock Monster", hp=80, damage=15)

