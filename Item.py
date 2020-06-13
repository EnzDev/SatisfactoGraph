from enum import Enum, auto


class ItemName(Enum):
    # Ores
    IRON_ORE = auto()
    COPPER_ORE = auto()

    # Tier 0 Component
    BIOMASS = auto()
    CABLE = auto()
    CONCRETE = auto()
    COPPER_INGOT = auto()
    IRON_INGOT = auto()
    IRON_PLATE = auto()
    IRON_ROD = auto()
    REINFORCED_IRON_PLATE = auto()
    SCREW = auto()
    WIRE = auto()

    # Tier 2 Component
    COPPER_SHEET = auto()
    SOLID_BIOFUEL = auto()
    MODULAR_FRAME = auto()
    ROTOR = auto()
    SMART_PLATING = auto()


class Item:
    item: ItemName
    quantity: int

    def __init__(self, name, quantity=1):
        self.item = name
        self.quantity = quantity
