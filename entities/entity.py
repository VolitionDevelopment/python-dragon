import random


class Entity(object):
    def __init__(self, name, max_hp, max_mana, attack_str, spells, items, statuses):
        self.name = name
        self.max_hp = max_hp
        self.health = max_hp
        self.max_mana = max_mana
        self.mana = max_mana
        self.attack_str = attack_str
        self.spells = spells
        self.items = items
        self.statuses = statuses

    def attack(self, target, attack_text):
        bonus = 1
        if random.randrange(0, 5) == 0:
            bonus *= 2
            attack_text += "\nCritical Hit!"

        print attack_text
        target.health -= random.randrange(self.attack_str - 2, self.attack_str + 3) * bonus

        return True

    def show_status(self):
        max = 40
        header = "=" * (max / 2 - 1 - (len(self.name) / 2)) + " " + self.name + " " + "=" * (max / 2 - 1 - (len(self.name) / 2))

        if len(header) == 41:
            header = header[:-1]

        print header
        print "Health: ", self.health, "/", self.max_hp
        print "Mana: ", self.mana, "/", self.max_mana
        print "=" * max
