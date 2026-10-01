import random

from players.player import Player

class RandomPlayer(Player):
    
    def __init__(self):
        super().__init__("Random")

    def act(self, env):
        return random.choice(env.get_action_space())