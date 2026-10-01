from loggers.game_logger import GameLogger
from loggers.simulation_logger import SimulationLogger
from environment.environment import Environment


class Simulation:

    def __init__(self, player, k = 10):

        self.id = 0
        self.player = player
        self.logger = SimulationLogger(k)
        self.scores = []

    def play_game(self):

        env = Environment(gameLogger = GameLogger(id = self.id, player_type = self.player.name))

        while not env.state.is_game_over:
        
            action = self.player.act(env)
            env.step(action)

        self.logger.log_game(env)
        return env.state.total_score

    def run(self, n):
        
        for i in range(n):
            self.scores.append(self.play_game())
            self.id += 1

            
        