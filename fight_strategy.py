from abc import ABC, abstractmethod


class FightStrategy(ABC):
    @abstractmethod
    def attack(self, target):
        pass

    def defend(self):
        pass


class Druid(FightStrategy):
    def attack(self, target):
        target.health -= 10
        print(f"Druid attacked {target.name}")
        print(f"{target.name} took 10 damage. Current health: {target.health}")

    def defend(self):
        self.health += 4
        print(
            "Druid defence"
        )  ### ??? AttributeError: 'Druid' object has no attribute 'health'?????


class Mage(FightStrategy):
    def attack(self, target):
        target.health -= 15
        print(f"Magic attack {target}")

    def defend(self):
        self.health += 5
        print("Magic defence")


class Rogue(FightStrategy):
    def attack(self, target):
        target.health -= 5
        print(f"Stealthy attack {target}")

    def defend(self):
        self.health += 2
        print("Stealthy defend")


class Warrior(FightStrategy):
    def attack(self, target):
        target.health -= 20
        print(f"Warrior attack {target}")

    def defend(self):
        self.health += 5
        print("Warrior defence")


class Archer(FightStrategy):
    def attack(self, target):
        target.health -= 10
        print(f"Archers attack {target}")

    def defend(self):
        self.health = target.attack() - 3  # ?????
        print("Archers defence")
