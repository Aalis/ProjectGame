from fight_strategy import Mage, Druid, Rogue, Warrior, Archer


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
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)


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
    p = TheMysticalDruid(name="jjj")
    p.display_stats()
    p.attack("Monster")
    p.defend()
