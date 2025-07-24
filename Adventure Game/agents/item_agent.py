import random

class ItemAgent:
    def give_item(self):
        items = ["Healing Potion", "Enchanted Sword", "Golden Key", "Mystic Ring"]
        return random.choice(items)
