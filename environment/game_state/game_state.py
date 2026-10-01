from environment.game_state.dice import Dice
from environment.game_state.board import Board

class GameState:

    def __init__(self):
        self.dice = Dice()
        self.board = Board()

        self.numTurns = 1
        self.numRolls = 1
        self.total_score = 0

        self.is_game_over = False

    def getSpace(self):
        state = {
            "numTurns" : self.numTurns,
            "numRolls" : self.numRolls,
            "score" : self.total_score,

            "dice" : self.dice.values,

            "scorecard" : self.board.scores,
            "categoriesTaken" : self.board.taken            
        }

        return state

    def reset(self):
        self.__init__()