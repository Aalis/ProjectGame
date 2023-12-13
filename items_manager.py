class EquipmentManager:
    def __init__(self, inventory):
        self.inventory = inventory
        self.__equiped_item = {
            "head": None,
            "chest": None,
            "r_hand": None,
            "l_hand": None,
            "legs": None,
        }

    def equip(self, item, body_part):
        if body_part in self.__equiped_item:
            if item in self.inventory.get_all_items():
                old_item = self.__equiped_item[body_part]
                if old_item is not None:
                    old_item.unequip()
                self.__equiped_item[body_part] = item
                print(f"equipped {item.name} on {body_part}")
            else:
                print(f"{item.name} is not in your inventory")
        else:
            print(f"{body_part} is not a valid body part")

    def unequip(self, body_part):
        self.__equiped_item[body_part] = None

    def get_equiped_items(self):
        return list(self.__equiped_item.values())

    def show_equiped_item(self):
        for body_part, item in self.__equiped_item.items():
            if item is not None:
                print(f"{body_part}: {item.name}")


class InventoryManager:
    def __init__(self):
        self.weapons = []
        self.potions = []
        self.armor = []

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def add_potion(self, potion):
        self.potions.append(potion)

    def add_armor(self, armor):
        self.armor.append(armor)

    def remove_potion(self, potion):
        self.potions.remove(potion)

    def get_all_items(self):
        return self.weapons + self.potions + self.armor

    def show_inventory(self):
        print("Weapons:")
        for weapon in self.weapons:
            print(f"- {weapon.name}")

        print("Potions:")
        for potion in self.potions:
            print(f"- {potion.name}")
        print("Armor:")
        for armor in self.armor:
            print(f"- {armor.name}")


class PotionManager:
    def __init__(self, inventory):
        self.inventory = inventory  #  TO DO!!!

    # def use_potion(self, potion):
    #     # if potion in self.inventory.potions:
    #     # if potion.effect == "health":
    #     self.health *= 1.2
    #     print(f"{self.name} healed 10 health. Current health: {self.health}")
    #     # elif potion.effect == "strength":
    #     self.strength += 2
    #     print(f"{self.name} gained 1 strength. Current strength: {self.strength}")
    #     # Remove the used potion from the inventory
    #     self.inventory.potions.remove(potion)

    # else:
    #     print(f"{self.name} does not have {potion.name} in their inventory.")
