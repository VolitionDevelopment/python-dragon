import potion
import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.max_health = 25
        self.health = self.max_health
        self.attack_str = 5
        self.magic_attack = 10
        self.mana = 15
        self.inventory = [
            potion.Potion(),
            potion.Potion()
        ]

    def attack(self, dragon):
        print "You struck the dragon with your mighty sword!"
        dragon.health -= random.randrange(self.attack_str - 2, self.attack_str + 3) if self.health > 5 else random.randrange(
            (self.attack_str * 2) - 2, (self.attack_str * 2) + 3)

        return True

    def spell(self, dragon):
        if self.mana >= 5:
            print "You used a spell on the dragon!"
            dragon.health -= self.magic_attack
            print ""
            return True
        else:
            print "You don't have enough mana..."
            return False

    def use_potion(self):
        if len(self.inventory) > 0:
            print "You used a potion. Your health is restored!"
            used_potion = self.inventory[0]
            used_potion.use(self)
            self.inventory.remove(used_potion)
            return True
        else:
            print "You don't have any potions!"
            return False

    def show_status(self):
        print "=================================="
        print "Hero Name: ", self.name
        print "Hero Health: ", self.health
        print "Hero Mana: ", self.mana
        print "==================================\n"
