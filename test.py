from fight_strategy import Mage, Druid


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


class TheMysticalDruid(BaseCharacter):
    def __init__(self, name):
        super().__init__(
            name,
            fight_strategy=Druid(),
            strength=1,
            agility=1,
            intelligence=1,
            experience=1,
            level=2,
            health=100,
        )


p = TheMysticalDruid("Ash")

p.attack("Monster")
p.defend()
