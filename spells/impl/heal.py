from spells.spell import Spell


class Heal(Spell):
    def __init__(self):
        Spell.__init__(self, "Heal", 10, 5)

    def fire(self, user, target):
        if user.mana >= self.mana_cost:
            print "%s used the spells %s" % (user.name, self.name)
            user.health += self.power
            if user.health > user.max_hp:
                user.health = user.max_hp
        else:
            print "%s doesn't have enough mana to use this spell!" % user.name
            return False
