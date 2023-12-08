from characters import *


class Battle:
    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2

    def start_battle(self):
        while True:
            # Character 1 attacks
            self.character1.attack(self.character2)

            self.check_win_condition()

            # Check if character 2 is still alive
            if self.character2.health <= 0:
                print(f"{self.character2.name} has died. {self.character1.name} wins!")
                self.handle_battle_result(self.character1, self.character2)
                break

            # Character 2 attacks
            self.character2.attack(self.character1)

            self.check_win_condition()

            # Check if character 1 is still alive
            if self.character1.health <= 0:
                print(f"{self.character1.name} has died. {self.character2.name} wins!")
                self.handle_battle_result(self.character2, self.character1)
                break

    def check_win_condition(self):
        # Check if either character's health is below or equal to 0
        if self.character1.health <= 0 or self.character2.health <= 0:
            return True
        return False

    def handle_battle_result(self, winner, loser):
        experience_gain = 50
        winner.gain_experience(experience_gain)
        winner.display_stats()


if __name__ == "__main__":
    # Create Character

    world = World()
    knife = Weapon("Knife", 40)
    flame_staff = Weapon("Flame Staff", 15)
    health_potion = HealthPotion("Health Potion")

    druid = TheMysticalDruid(name="Druid")
    rogue = TheStealthyRogue(name="Rogue")

    world.add_character(druid)
    world.add_character(rogue)

    druid.equip_weapon(flame_staff)
    rogue.equip_weapon(knife)
    druid.inventory.add_potion(health_potion)

    # Start the battle
    battle = Battle(druid, rogue)
    battle.start_battle()
