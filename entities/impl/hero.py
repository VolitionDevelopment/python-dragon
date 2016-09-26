from entities.entity import Entity
from items.impl import health_potion
from items.impl import mana_potion
from spells.impl import fireball
from spells.impl import ice_storm
from spells.impl import poison


class Hero(Entity):
    def __init__(self, name):
        super(Hero, self).__init__(name, 30, 20, 5, [
            fireball.Fireball(),
            ice_storm.IceStorm(),
            poison.Poison()
        ], [
            health_potion.HealthPotion(),
            mana_potion.ManaPotion()
        ], [])
        self.name = name
