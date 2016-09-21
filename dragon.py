import random

class Dragon:
    def __init__(self):
        self.max_health = 40
        self.health = self.max_health
        self.attack_str = 5
        self.magic_attack = 8
        self.mana = 20

    def attack(self, hero):
        print "The dragon stuck you with it's mighty claws!"
        hero.health -= random.randrange(self.attack_str - 2, self.attack_str + 3)

    def breathe_fire(self, hero):
        print "The dragon breathed fire in your face!"
        hero.health -= self.magic_attack
        self.mana -= 5

    def heal(self):
        print "The dragon used a spell! It's health was restored."
        self.health += 8
        if self.health > self.max_health:
            self.health = self.max_health

        self.mana -= 5

    def show_status(self):
        print "=================================="
        print "Dragon Health: ", self.health
        print "Dragon Mana: ", self.mana
        print "==================================\n"
