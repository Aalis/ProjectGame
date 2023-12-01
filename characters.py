from fight_strategy import Mage, Druid, Rogue, Warrior, Archer
from magic_items import HealthPotion, HeavyAttack
from functools import wraps


class World:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(World, cls).__new__(cls)
            cls._instance.character = []
        return cls._instance

    def add_character(self, character):
        self.character.append(character)

    def show_characters(self):
        print(f"Characters in the world:")
        for character in self.character:
            print(f"- {character.name}")


class BaseCharacter:
    def __init__(
        self,
        name,
        strength,
        agility,
        intelligence,
        experience,
        level,
        health,
        fight_strategy=None,
    ):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.experience = experience
        self.level = level
        self.health = health
        self.fight_strategy = fight_strategy
        self.inventory = Inventory()

    def attack(self, target):
        return self.fight_strategy.attack(target)

    def defend(self):
        return self.fight_strategy.defend()

    def display_stats(self):
        print(f"Name: {self.name}, Strength: {self.strength}, Health: {self.health}")


class Equipment:
    def __init__(self):
        self.__equiped_item = {
            "head": None,
            "chest": None,
            "r_hand": None,
            "l_hand": None,
            "legs": None,
        }

    def equip(self, item, body_part):
        self.__equiped_item[body_part] = item

    def show_equiped_item(self):
        for body_part, item in self.__equiped_item.items():
            if item is not None:
                print(body_part, item.name)


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def use_item(self, item_name, target):
        if item_name in self.items:
            self.items[item_name].use(target)
        else:
            print(f"{item_name} not in inventory")

    def show_inventory(self):
        item_str = ", ".join(
            f"{item.name}: {item.amount} points" for item in self.items.values()
        )
        print(f"Inventory: {item_str}")


class TheElementalMage(BaseCharacter):
    def __init__(self, name):
        super().__init__(
            name,
            fight_strategy=Mage(),
            strength=1,
            agility=1,
            intelligence=1,
            experience=1,
            level=1,
            health=100,
        )


class TheStealthyRogue(BaseCharacter):
    def __init__(self, name):
        super().__init__(
            name,
            fight_strategy=Rogue(),
            strength=1,
            agility=1,
            intelligence=1,
            experience=1,
            level=1,
            health=100,
        )


class TheResillientWarrior(BaseCharacter):
    def __init__(self, name):
        super().__init__(
            name,
            fight_strategy=Warrior(),
            strength=1,
            agility=1,
            intelligence=1,
            experience=1,
            level=1,
            health=100,
        )


class TheSkilledArcher(BaseCharacter):
    def __init__(self, name):
        super().__init__(
            name,
            fight_strategy=Archer(),
            strength=1,
            agility=1,
            intelligence=1,
            experience=1,
            level=1,
            health=100,
        )


class TheMysticalDruid(BaseCharacter):
    def __init__(self, name):
        super().__init__(
            name,
            fight_strategy=Druid(),
            strength=1,
            agility=1,
            intelligence=1,
            experience=1,
            level=1,
            health=100,
        )


if __name__ == "__main__":
    # Create Character
    p1 = TheMysticalDruid(name="Druid")
    p2 = TheStealthyRogue(name="Rogue")

    world = World()
    world.add_character(p1)
    world.add_character(p2)
    world.show_characters()

    # Create Items
    health_potion = HealthPotion(name="Health_Potion", amount=10)
    heavy_attack = HeavyAttack(name="Heavy_Attack", amount=10)

    # Add Items to character
    p1.inventory.add_item(health_potion)
    p1.inventory.add_item(heavy_attack)
    p1.inventory.show_inventory()
    p1.inventory.use_item("Health_Potion", p1)

    p1.display_stats()
    p2.display_stats()
    p1.attack(p2)
    p1.defend()
