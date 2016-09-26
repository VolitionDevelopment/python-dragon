from spells.spell import Spell


class IceStorm(Spell):
    def __init__(self):
        Spell.__init__(self, "Ice Storm", 6, 8)

    def fire(self, user, target):
        pass
