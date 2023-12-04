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
            print(
                f"- {character.name}: Health={character.health}, Strength={character.strength}"
            )


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
    ):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.experience = experience
        self.level = level
        self.health = health
        self.inventory = Inventory()

    def attack(self, target):
        pass

    def defend(self):
        pass

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
    def health_boost(character):
        character.health += 10
        print(f"{character.name} healed 10 health. Current health: {character.health}")

        return character

    def strength_boost(character):
        character.strength += 2
        print(
            f"{character.name} gained 1 strength. Current strength: {character.strength}"
        )

        return character

    def agility_boost(character):
        character.agility += 2
        print(
            f"{character.name} gained 1 agility. Current agility: {character.agility}"
        )

        return character


class TheElementalMage(BaseCharacter):
    def __init__(self, name):
        super().__init__(
            name,
            strength=1,
            agility=1,
            intelligence=1,
            experience=1,
            level=1,
            health=100,
        )

    def throw_fireball(self, target):
        target.health -= 10
        print(f"{target.name} took 10 damage. Current health: {target.health}")

    def attack(self, target):
        self.throw_fireball(target)


class TheStealthyRogue(BaseCharacter):
    def __init__(self, name):
        super().__init__(
            name,
            strength=1,
            agility=1,
            intelligence=1,
            experience=1,
            level=1,
            health=100,
        )

    def backstab(self, target):
        target.health -= 10
        print(f"{target.name} took 10 damage. Current health: {target.health}")

    def attack(self, target):
        self.backstab(target)


class TheResillientWarrior(BaseCharacter):
    def __init__(self, name):
        super().__init__(
            name,
            strength=1,
            agility=1,
            intelligence=1,
            experience=1,
            level=1,
            health=100,
        )

    def axe_strike(self, target):
        target.health -= 7
        print(f"{target.name} took 10 damage. Current health: {target.health}")

    def attack(self, target):
        self.axe_strike(target)


class TheSkilledArcher(BaseCharacter):
    def __init__(self, name):
        super().__init__(
            name,
            strength=1,
            agility=1,
            intelligence=1,
            experience=1,
            level=1,
            health=100,
        )

    def bow_shoot(self, target):
        target.health -= 5
        print(f"{target.name} took 10 damage. Current health: {target.health}")

    def attack(self, target):
        self.bow_shoot(target)


class TheMysticalDruid(BaseCharacter):
    def __init__(self, name):
        super().__init__(
            name,
            strength=1,
            agility=1,
            intelligence=1,
            experience=1,
            level=1,
            health=100,
        )

    def cast_spell(self, target):
        target.health -= 5
        print(f"{target.name} took 10 damage. Current health: {target.health}")

    def attack(self, target):
        self.cast_spell(target)


if __name__ == "__main__":
    # Create Character
    p1 = TheMysticalDruid(name="Druid")
    p2 = TheStealthyRogue(name="Rogue")

    world = World()
    world.add_character(p1)
    world.add_character(p2)
    world.show_characters()

    # Apply boost items on character
    Inventory.health_boost(p1)
    Inventory.strength_boost(p1)

    p2.backstab(p1)

    p1.display_stats()
    p2.display_stats()
