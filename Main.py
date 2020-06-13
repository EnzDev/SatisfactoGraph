from typing import Dict

from Craft import Craft
from Item import ItemName
from importer import create_craft_rule
from utils import second_to_pretty, print_need, plot_rules

if __name__ == "__main__":
    rules = create_craft_rule("craft.data")
    plot_rules(rules)

    rules_graphed: Dict[ItemName, Craft] = {
        craft.to_item.item: craft for craft in rules
    }

    craft_item_name = input("What to craft ?\n").upper().replace(" ", "_")
    craft_item = ItemName[craft_item_name]

    amount = int(input("Amount: "))

    total_time = print_need(rules_graphed, craft_item, amount)

    print("Total amount of craft time: %s" % second_to_pretty(total_time))
