class Potion:
    def __init__(self):
        self.heal_amt = 20

    def use(self, hero):
        hero.health += self.heal_amt
        if hero.health > hero.max_health:
            hero.health = hero.max_health
