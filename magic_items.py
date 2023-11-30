from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name):
        self.name = name

        @abstractmethod
        def use(self, target):
            pass


class HealthPotion(Item):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount
        print(f"{self.name} created with healing amount {self.amount}")

    def use(self, target):
        target.health += self.amount
        print(f"{target.name} healed for {self.amount} health")


class HeavyAttack(Item):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount
        print(f"{self.name} created with attack amount {self.amount}")

    def use(self, target):
        target.health -= self.amount
        print(f"{target.name} took {self.amount} damage")
