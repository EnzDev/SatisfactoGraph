from typing import Dict, List

from Craft import Craft
from Item import ItemName


def second_to_pretty(total_seconds):
    seconds = total_seconds % 60
    minutes = (total_seconds // 60) % 60
    hours = (total_seconds // 60) // 60

    time = "%ds" % seconds
    if minutes > 0 or hours > 0:
        time = "%dm " % minutes + time
    if hours > 0:
        time = "%dh " % hours + time
    return time


def print_need(rules_graphed: Dict[ItemName, Craft], craft_item: ItemName, q=1, deep=0):
    craft = rules_graphed[craft_item]
    craft_rounds = q // craft.to_item.quantity + (q % craft.to_item.quantity > 0)
    print("\t" * deep + "%s x %d (%ds)" % (
        craft.to_item.item,
        craft.to_item.quantity * craft_rounds,
        craft_rounds * craft.time
    )
          )

    time_to_craft = craft_rounds * craft.time

    for source in craft.from_item:
        if source.item in rules_graphed:
            time_to_craft += print_need(rules_graphed, rules_graphed[source.item], source.quantity * craft_rounds, deep + 1)

    return time_to_craft


def plot_rules(rules: List[Craft]) -> None:
    import networkx as nx
    from matplotlib import pyplot

    pyplot.figure(figsize=(30, 30))
    G = nx.MultiDiGraph(directed=True)
    values = {}
    for craft in rules:
        for source in craft.from_item:
            G.add_edges_from([(source.item.name, craft.to_item.item.name)], lab=craft.label(source))
        values[craft.to_item.item.name] = craft.time

    edge_labels = dict([((u, v,), d["lab"]) for u, v, d in G.edges(data=True)])
    pos = nx.fruchterman_reingold_layout(G, k=0.7, iterations=100, scale=5)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx(G, pos, with_labels=True, node_size=3000, node_color=[values.get(node, 0) for node in G.nodes()])
    pyplot.show()
