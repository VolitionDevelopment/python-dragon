import potion
import random

import spell


class Hero:
    def __init__(self, name):
        self.name = name
        self.max_health = 25
        self.health = self.max_health
        self.attack_str = 5
        self.mana = 15
        self.inventory = [
            potion.Potion("Health Potion", "Health", 20),
            potion.Potion("Health Potion", "Health", 20),
            potion.Potion("Mana Potion", "Mana", 10)
        ]
        self.spells = [
            spell.Spell("Fireball", 10, 5),
            spell.Spell("Ice", 12, 6)
        ]

    def attack(self, dragon):
        print "You struck the dragon with your mighty sword!"
        dragon.health -= random.randrange(self.attack_str - 2,
                                          self.attack_str + 3) if self.health > 5 else random.randrange(
            (self.attack_str * 2) - 2, (self.attack_str * 2) + 3)

        return True

    def show_status(self):
        print "=================================="
        print "Hero Name: ", self.name
        print "Hero Health: ", self.health
        print "Hero Mana: ", self.mana
        print "==================================\n"
