from items.item import Item


class Consumable(Item):
    def __init__(self, name, type):
        super(Consumable, self).__init__(name, type)

    def use(self, user):
        pass
