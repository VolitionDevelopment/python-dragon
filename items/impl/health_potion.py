from items.consumable import Consumable


class HealthPotion(Consumable):
    def __init__(self):
        super(HealthPotion, self).__init__("Health Potion", "Health")
        self.power = 20

    def use(self, user):
        print "You have restored your health!"
        user.health += self.power
        if user.health > user.max_health:
            user.health = user.max_health
        return True
