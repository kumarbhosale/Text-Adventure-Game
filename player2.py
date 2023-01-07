import items


class Player2():
    def __init__(self):
        self.name = Player2
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.name

class Trader(Player2):
    def __init__(self):
        super().__init__()
        self.name = "Trader"
        self.gold = 100
        self.inventory = [items.FreshBread(),
                      items.FreshBread(),
                      items.FreshBread(),
                      items.HealingPotion(),
                      items.HealingPotion()]
