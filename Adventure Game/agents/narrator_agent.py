import random

class NarratorAgent:
    def intro(self):
        return "You wake up in the Forgotten Forest. A whisper in the wind tells of a lost treasure beyond the mist."

    def generate_event(self):
        events = [
            {"text": "You find a glowing chest hidden in the roots of an ancient tree.", "enemy": False},
            {"text": "A shadow rises... An enemy appears!", "enemy": True},
            {"text": "You discover a hidden cave with flickering torches.", "enemy": False},
            {"text": "A goblin jumps from the bushes, snarling!", "enemy": True},
            {"text": "You come across a peaceful waterfall shimmering with light.", "enemy": False},
            {"text": "A pack of wolves growls in the distance — one leaps at you!", "enemy": True},
            {"text": "You step on an old scroll buried under moss.", "enemy": False},
            {"text": "An eerie silence surrounds you... something is watching.", "enemy": True},
            {"text": "A wise owl drops a shiny object at your feet.", "enemy": False},
            {"text": "The trees whisper in an unknown language...", "enemy": False}
        ]

        return random.choice(events)
