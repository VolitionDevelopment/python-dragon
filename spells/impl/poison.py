from spells.spell import Spell


class Poison(Spell):
    def __init__(self):
        Spell.__init__(self, "Poison Cloud", 3, 15)

    def fire(self, user, target):
        pass
