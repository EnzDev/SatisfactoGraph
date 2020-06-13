from typing import List

from Craft import Craft
from Item import ItemName, Item


def create_craft_rule(file_input) -> List[Craft]:
    crafts = []

    with open(file_input) as file:
        while True:
            line = file.readline().rstrip("\n")

            craft = []
            while line != "":
                craft.append(line)
                line = file.readline().rstrip("\n")

            if len(craft) == 0:
                break

            time, energy = [int(v) for v in craft.pop().split(" ")]
            crafts.append(Craft(
                {item_decode(item) for item in craft[:-1]},
                item_decode(craft[-1]),
                time, energy
            ))
    return crafts


def item_decode(line):
    to_item_name, to_item_q = line.split(" ")
    return Item(ItemName[to_item_name], int(to_item_q))