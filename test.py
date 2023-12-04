class Character:
    def __init__(self, name, health=100, strength=10):
        self.name = name
        self.health = health
        self.strength = strength

    def display_status(self):
        print(f"{self.name}: Health={self.health}, Strength={self.strength}")


def health_booster(character):
    character.health += 10
    print(f"{character.name} healed 10 health. Current health: {character.health}")
    return character


charact = Character("Test")
charact.display_status()
health_booster(charact)
health_booster(charact)
health_booster(charact)
charact.display_status()
