
import items, enemies, actions, world
 
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
 
    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
 
        return moves


class StartingRoom(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return"""
        Somewhere nearby is a cave, where others have found fortunes in
        treasure and gold, though it is rumored that some who enter are
        never seen again!!! Magic is said to work in the cave....
    
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """

    def modify_player(self, player):
        #Room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory.append(self.item)
 
    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
 
class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """

class WolfRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Wolf())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """

class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())
 
    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """

class FindSwordRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.RustySword())

    def intro_text(self):
        return """
        Your notice something shiny in the middle of the ground.
        It's a Sword! You pick it up.
        """

class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
 
 
        Victory is yours!
        """
    def modify_player(self, player):
        player.victory = True

class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
            super().__init__(x, y, items.Gold(5))

    def intro_text(self):
            return """
            Someone dropped a 5 gold piece. You pick it up.
            """

class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
            super().__init__(x, y, enemies.Ogre())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
                An ogre is blocking your path!
                """
        else:
            return """
                A dead ogre reminds you of your triumph.
                """

class SnakePitRoom(MapTile):
    def intro_text(self):
        return """
            You have fallen into a pit of deadly snakes!
            You have died!
            """

    def modify_player(self, player):
            player.hp = 0

class BatColony(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.BatColony())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You hear a squeaking noise growing louder
            ... suddenly you are lost in swarm of bats! 
            """
        else:
            return """
            Dozens of dead bats are scattered on the ground. 
            """

class RockMonster(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.RockMonster())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You've disturbed a rock monster from his slumber!
            """
        else:
            return """
            Defeated, the monster has reverted into a ordinary rock.
            """

class FindCrossbow(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Crossbow())

    def intro_text(self):
        return """
        You find a deadly killer weapon. Crossbow!
        """

class Mazeltov(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Mazeltov())

    def intro_text(self):
        return """
        You find a roasting weapon. Mazeltov!
        """

class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("Here's whats available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['S', 's']:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")

    def intro_text(self):
        return """
        A frail not-quite-human, not-quite-creature squats in the corner
        clinking his gold coins together. He looks willing to trade.
        """
