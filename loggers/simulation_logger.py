from copy import deepcopy
import pandas as pd


class SimulationLogger:

    def __init__(self, k):
        self.k = k
        self.top_k_games = []
        self.bottom_k_games = []

        cols = [

            "id",
            "player_type",
            "total_score",
            "total_reward"
        
        ]

        for i in range(11):
            cols.append(f"score_{i}")
        
        self.summary = pd.DataFrame(columns = cols)

    def log_game(self, env):

        currScore = env.gameLogger.total_score
        
        if len(self.top_k_games) < self.k:
            self.top_k_games.append(deepcopy(env.gameLogger))
            self.top_k_games.sort(key=lambda game: game.total_score, reverse=True)
        
        elif currScore > self.top_k_games[-1].total_score:
            self.top_k_games.append(deepcopy(env.gameLogger))
            self.top_k_games.sort(key=lambda game: game.total_score, reverse=True)
            self.top_k_games = self.top_k_games[:self.k]
        
        
        if len(self.bottom_k_games) < self.k:
            self.bottom_k_games.append(deepcopy(env.gameLogger))
            self.bottom_k_games.sort(key=lambda game: game.total_score)
        
        elif currScore < self.bottom_k_games[-1].total_score:
            self.bottom_k_games.append(deepcopy(env.gameLogger))
            self.bottom_k_games.sort(key=lambda game: game.total_score)
            self.bottom_k_games = self.bottom_k_games[:self.k]
        
        
        self.summary.loc[len(self.summary)] = env.gameLogger.get_summary()

        