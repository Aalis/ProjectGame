from items_manager import *


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
        self, name, strength, agility, intelligence, experience, level, health, weapon
    ):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.experience = experience
        self.level = level
        self.health = health
        self.weapon = None
        self.inventory = InventoryManager()
        self.potion_manager = PotionManager(self.inventory)
        self.equipment = EquipmentManager(self.inventory)

    def gain_experience(self, experience):
        self.experience += experience
        print(
            f"{self.name} gained {experience} experience. Current experience: {self.experience}"
        )
        experience_needed = self.level * 100
        while self.experience > experience_needed:
            self.level_up()
            experience_needed = self.level * 100

    def level_up(self):
        self.level += 1
        print(f"{self.name} has leveled up to level {self.level}")
        self.strength += 2
        self.agility += 1
        self.health += 10
        self.intelligence += 1

    def display_stats(self):
        print(
            f"Name: {self.name}, Strength: {self.strength}, Health: {self.health}, Level: {self.level}, Experience: {self.experience}"
        )


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


class TheStealthyRogue(BaseCharacter):
    def __init__(self, name):
        super().__init__(
            name,
            strength=1,
            agility=1,
            intelligence=1,
            experience=1,
            level=1,
            weapon=None,
            health=100,
        )


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


class TheMysticalDruid(BaseCharacter):
    def __init__(self, name):
        super().__init__(
            name,
            strength=1,
            agility=1,
            intelligence=1,
            experience=1,
            level=1,
            weapon=None,
            health=100,
        )
