from tools import roll_dice
import random

class MonsterAgent:
    def fight(self, current_health: int):
        dice = roll_dice()  

        if dice >= 4:
            damage = random.randint(5, 20)
            return {
                "won": True,
                "health": current_health - damage,
                "text": f"You won the fight! But lost {damage} health."
            }
        else:
            return {
                "won": False,
                "health": 0,
                "text": "The monster defeated you... better luck next time!"
            }
