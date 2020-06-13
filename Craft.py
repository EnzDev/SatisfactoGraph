from typing import Set

from Item import Item


class Craft:
    def __init__(self, from_item: Set[Item], to_item: Item, time=0, energy=0):
        self.from_item = from_item
        self.to_item = to_item
        self.time = time
        self.energy = energy

    def label(self, from_item: Item):
        return "Cost: %d\nProduce: %d\n%d s (%d MJ/i)\n" % (
            from_item.quantity,
            self.to_item.quantity,
            self.time,
            self.energy
        )
