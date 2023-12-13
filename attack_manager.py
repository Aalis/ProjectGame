from enum import Enum


class ItemType(Enum):
    WEAPON = 1
    POTION = 2
    ARMOR = 3


class Item:
    def __init__(self, name, type):
        self.name = name
        self.type = type


class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__(name, type=ItemType.WEAPON)
        self.name = name
        self.damage = damage


class Potion(Item):
    def __init__(self, name, effect):
        super().__init__(name, type=ItemType.POTION)
        self.name = name
        self.effect = effect


class Armor(Item):
    def __init__(self, name, defense):
        super().__init__(name, type=ItemType.ARMOR)
        self.name = name
        self.defense = defense


class Fight:
    def attack(self, attacker, target):
        #  Armed attack
        for item in attacker.equipment.get_equiped_items():
            if item is not None and item.type == ItemType.WEAPON:
                target.health -= item.damage * attacker.strength
                print(
                    f"{attacker.name} attacked {target.name} with {item.name} for {item.damage*attacker.strength} damage"
                )
                break
        # Armor defense
        for item in target.equipment.get_equiped_items():
            if item is not None and target.health < 50 and item.type == ItemType.ARMOR:
                target.health += item.defense
                print(f"{target.name} used {item.name}.")

                break
        # Unarmed attack
        if all(
            item is None or item.type != ItemType.WEAPON
            for item in attacker.equipment.get_equiped_items()
        ):
            target.health -= attacker.strength
            print(
                f"{attacker.name} attacked {target.name} with an unarmed strike for {attacker.strength} damage"
            )
            # Armor defense
            for item in target.equipment.get_equiped_items():
                if (
                    item is not None
                    and target.health < 50
                    and item.type == ItemType.ARMOR
                ):
                    target.health += item.defense
                    print(f"{target.name} used {item.name}.")
                    break

        # Use health potion if possible
        if target.health < 50:
            health_potion = next(
                (
                    potion
                    for potion in target.inventory.potions
                    if potion.effect == "health"
                ),
                None,
            )
            if health_potion:
                target.health += 10
                print(f"{target.name} healed for 10 health.")
