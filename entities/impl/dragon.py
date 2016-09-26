import random

from entities.entity import Entity
from spells.impl import fireball
from spells.impl import heal


class Dragon(Entity):
    def __init__(self):
        super(Dragon, self).__init__("The Dragon", 50, 15, 8, [
            heal.Heal(),
            fireball.Fireball()
        ], [], [])
