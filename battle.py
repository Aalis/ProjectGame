from characters import *
from attack_manager import *


class Battle:
    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2

    def start_battle(self):
        fight = Fight()
        while not self.check_win_condition():
            # Character 1 attacks
            fight.attack(self.character1, self.character2)
            self.display_stats()

            # Check if character 2 is still alive
            if self.character2.health <= 0:
                print(f"{self.character2.name} has died. {self.character1.name} wins!")
                self.handle_battle_result(self.character1, self.character2)
                break

            # Character 2 attacks
            fight.attack(self.character2, self.character1)
            self.display_stats()

            # Check if character 1 is still alive
            if self.character1.health <= 0:
                print(f"{self.character1.name} has died. {self.character2.name} wins!")
                self.handle_battle_result(self.character2, self.character1)
                break

    def check_win_condition(self):
        # Check if either character's health is below or equal to 0
        return self.character1.health <= 0 or self.character2.health <= 0

    def handle_battle_result(self, winner, loser):
        experience_gain = 50
        winner.gain_experience(experience_gain)
        winner.display_stats()

    def display_stats(self):
        print(f"{self.character1.name}: Health={self.character1.health}")
        print(f"{self.character2.name}: Health={self.character2.health}")


# Create characters and items
world = World()
flame_staff = Weapon("Flame Staff", 15)
knife = Weapon("Knife", 40)
shield = Armor("Shield", 20)
sword = Weapon("Sword", 30)
helmet = Armor("Helmet1", 10)
helmet2 = Armor("Helmet2", 10)
helmet3 = Armor("Helmet3", 10)
health_potion = Potion("Potion", "health")


druid = TheMysticalDruid(name="Druid")
rogue = TheStealthyRogue(name="Rogue")

druid.inventory.add_weapon(flame_staff)
rogue.inventory.add_weapon(knife)
druid.inventory.add_potion(health_potion)
rogue.inventory.add_armor(shield)
druid.inventory.add_armor(helmet)

world.add_character(druid)
world.add_character(rogue)

rogue.equipment.equip(knife, "l_hand")
rogue.equipment.equip(shield, "chest")
rogue.equipment.equip(sword, "r_hand")
druid.equipment.equip(helmet, "head")
druid.equipment.equip(helmet2, "head")
druid.equipment.equip(helmet3, "legs")

# Start the battle
battle = Battle(druid, rogue)
battle.start_battle()
