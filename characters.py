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
        self, name, strength, agility, intelligence, experience, level, health=100
    ):
        super().__init__(
            name, strength, agility, intelligence, experience, level, health
        )
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.experience = experience
        self.level = level
        self.health = health
        self._inventory = Inventory()
        self, _equipment = Equipment()

    def attack(self, target):
        pass

    def defence(self, target):
        pass
