class BaseCharacter:
    def __init__(
        self, name, strength, agility, intelligence, experience, level, health=100
    ):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.experience = experience
        self.level = level
        self.health = health

    def attack(self, target):
        pass

    def defence(self, target):
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
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)


class TheElementalMage(BaseCharacter):
    def __init__(
        self, name, strength, agility, intelligence, experience, level, health
    ):
        super().__init__(
            name, strength, agility, intelligence, experience, level, health
        )

    def attack(self, target):
        # TODO:special attack
        pass

    def defence(self, target):
        # TODO:special defence
        pass


class TheStealthyRogue(BaseCharacter):
    def __init__(
        self, name, strength, agility, intelligence, experience, level, health
    ):
        super().__init__(
            name, strength, agility, intelligence, experience, level, health
        )

    def attack(self, target):
        # TODO:special attack
        pass

    def defence(self, target):
        # TODO:special defence
        pass


class TheResillientWarrior(BaseCharacter):
    def __init__(
        self, name, strength, agility, intelligence, experience, level, health
    ):
        super().__init__(
            name, strength, agility, intelligence, experience, level, health
        )

    def attack(self, target):
        # TODO:special attack
        pass

    def defence(self, target):
        # TODO:special defence
        pass


class TheSkilledArcher(BaseCharacter):
    def __init__(
        self, name, strength, agility, intelligence, experience, level, health
    ):
        super().__init__(
            name, strength, agility, intelligence, experience, level, health
        )

    def attack(self, target):
        # TODO:special attack
        pass

    def defence(self, target):
        # TODO:special defence
        pass


class TheMysticalDruid(BaseCharacter):
    def __init__(
        self, name, strength, agility, intelligence, experience, level, health
    ):
        super().__init__(
            name, strength, agility, intelligence, experience, level, health
        )

    def attack(self, target):
        # TODO:special attack
        pass

    def defence(self, target):
        # TODO:special defence
        pass


if __name__ == "__main__":
    p = TheMysticalDruid(
        name="Dron",
        strength=89,
        agility=9,
        experience=8,
        level=0,
        intelligence=98,
        health=100,
    )
    p.display_stats()
