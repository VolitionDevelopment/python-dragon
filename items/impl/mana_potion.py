from items.consumable import Consumable


class ManaPotion(Consumable):
    def __init__(self):
        super(ManaPotion, self).__init__("Mana Potion", "Mana")
        self.power = 15

    def use(self, user):
        print "You have restored your mana!"
        user.mana += self.power
        return True
