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


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Potion:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect


class HealthPotion(Potion):
    def __init__(self, name):
        super().__init__(name, effect="health")

    def apply(self, character):
        character.use_potion(self)


class BaseCharacter:
    def __init__(
        self,
        name,
        strength,
        agility,
        intelligence,
        experience,
        level,
        weapon,
        health,
    ):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.experience = experience
        self.level = level
        self.weapon = None
        self.health = health
        self.inventory = Inventory()

    def attack(self, target):
        pass

    def defend(self):
        pass

    def gain_experience(self, experience):
        self.experience += experience
        print(
            f"{self.name} gained {experience} experience. Current experience: {self.experience}"
        )
        while self.experience >= self.level * 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        print(f"{self.name} has leveled up to level {self.level}")
        self.strength += 2
        self.agility += 1
        self.health += 10
        self.intelligence += 1

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} equipped {weapon.name}")

    def use_potion(self, potion):
        if potion in self.inventory.potions:
            if potion.effect == "health":
                self.health *= 1.2
                print(f"{self.name} healed 10 health. Current health: {self.health}")
            elif potion.effect == "strength":
                self.strength += 2
                print(
                    f"{self.name} gained 1 strength. Current strength: {self.strength}"
                )
            # Remove the used potion from the inventory
            self.inventory.potions.remove(potion)
        else:
            print(f"{self.name} does not have {potion.name} in their inventory.")

    def display_stats(self):
        print(
            f"Name: {self.name}, Strength: {self.strength}, Health: {self.health}, Level: {self.level}, Experience: {self.experience}"
        )


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
        self.weapons = []
        self.potions = []

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def add_potion(self, potion):
        self.potions.append(potion)

    def show_inventory(self):
        print("Weapons:")
        for weapon in self.weapons:
            print(f"- {weapon.name}")

        print("Potions:")
        for potion in self.potions:
            print(f"- {potion.name}")


class TheElementalMage(BaseCharacter):
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

    def attack(self, target):
        if self.weapon is not None:
            damage = self.weapon.damage * self.strength
            target.health -= damage
            print(f"{self.name} attacked with {self.weapon.name}!")
            print(f"{target.name}'s health: {target.health}")
        else:  # unarmed attack
            target.health -= self.strength
            print(f"{self.name} attacked with an unarmed strike!")
            print(f"{target.name}'s health: {target.health}")


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

    def attack(self, target):
        if self.weapon is not None:
            damage = self.weapon.damage * self.strength
            target.health -= damage
            print(f"{self.name} attacked with {self.weapon.name}!")
            print(f"{target.name}'s health: {target.health}")
        else:  # unarmed attack
            target.health -= self.strength
            print(f"{self.name} attacked with an unarmed strike!")
            print(f"{target.name}'s health: {target.health}")


class TheResillientWarrior(BaseCharacter):
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

    def attack(self, target):
        if self.weapon is not None:
            damage = self.weapon.damage * self.strength
            target.health -= damage
            print(f"{self.name} attacked with {self.weapon.name}!")
            print(f"{target.name}'s health: {target.health}")
        else:  # unarmed attack
            target.health -= self.strength
            print(f"{self.name} attacked with an unarmed strike!")
            print(f"{target.name}'s health: {target.health}")


class TheSkilledArcher(BaseCharacter):
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

    def attack(self, target):
        if self.weapon is not None:
            damage = self.weapon.damage * self.strength
            target.health -= damage
            print(f"{self.name} attacked with {self.weapon.name}!")
            print(f"{target.name}'s health: {target.health}")
        else:  # unarmed attack
            target.health -= self.strength
            print(f"{self.name} attacked with an unarmed strike!")
            print(f"{target.name}'s health: {target.health}")


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

    def attack(self, target):
        if self.weapon is not None:
            damage = self.weapon.damage * self.strength
            target.health -= damage
            print(f"{self.name} attacked with {self.weapon.name}!")
            print(f"{target.name}'s health: {target.health}")
        else:  # unarmed attack
            target.health -= self.strength
            print(f"{self.name} attacked with an unarmed strike!")
            print(f"{target.name}'s health: {target.health}")
