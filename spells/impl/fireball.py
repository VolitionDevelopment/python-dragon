from spells.spell import Spell


class Fireball(Spell):
    def __init__(self):
        Spell.__init__(self, "Fireball", 10, 5)
