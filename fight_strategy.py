from abc import ABC, abstractmethod


class FightStrategy(ABC):
    @abstractmethod
    def attack(self, target):
        pass

    def defend(self):
        pass


class Druid(FightStrategy):
    def attack(self, target):
        print(f"Druid attacking {target}")
        return

    def defend(self):
        print("Druid defence")


class Mage(FightStrategy):
    def attack(self, target):
        print(f"Magic attack {target}")

    def defend(self):
        print("Magic defence")


class Rogue(FightStrategy):
    def attack(self, target):
        print(f"Stealthy attack {target}")

    def defend(self):
        print("Stealthy defend")


class Warrior(FightStrategy):
    def attack(self, target):
        print(f"Warrior attack {target}")

    def defend(self):
        print("Warrior defence")


class Archer(FightStrategy):
    def attack(self, target):
        print(f"Archers attack {target}")

    def defend(self):
        print("Archers defence")
