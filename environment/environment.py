from copy import deepcopy

from loggers.game_logger import GameLogger
from environment.game_state.action import Action
from environment.game_state.game_state import GameState

from reward_functions.default_reward import defaultReward

class Environment:

    def __init__(self, render_mode = None, gameLogger = None, rewardFunction = defaultReward):

        self.render_mode = render_mode
        self.rewardFunction = rewardFunction
        
        if gameLogger is None:
            gameLogger = GameLogger()

        self.gameLogger = gameLogger
        self.reset()

    def get_observation_space(self):
        return self.state.getSpace()

    def get_action_space(self):
        actions = []

        if self.state.numTurns > 11:
            return actions

        
        if self.state.numRolls <= 2:
            action = Action("roll")
            actions.append(action)

        for idx in self.state.board.get_available_categories():
            action = Action("pick", category = idx)
            actions.append(action)

        return actions

    def reset(self):
        self.state = GameState()
        
        self.state.dice.roll()
        self.gameLogger.log_initial_roll(self.state, self.get_available_scores(), self.state.board.get_available_categories())
        
        self.observation_space = self.get_observation_space()

    def calculate_category_score(self, idx):

        if idx in range(6):
            return self.state.dice.frequency()[idx + 1] * (idx + 1)

        if idx == 6:
            if max(self.state.dice.frequency().values()) >= 3:
                return self.state.dice.sum()
            return 0

        if idx == 7:
            if max(self.state.dice.frequency().values()) >= 4:
                return self.state.dice.sum()
            return 0
            
        if idx == 8:
            if self.state.dice.sorted() == [1,2,3,4,5] or self.state.dice.sorted() == [2,3,4,5,6]:
                return 40
            else:
                return 0
                
        if idx == 9:
            if 2 in self.state.dice.frequency().values() and 3 in self.state.dice.frequency().values():
                return 25
            else:
                return 0
                
        if idx == 10:
            if max(self.state.dice.frequency().values()) == 5:
                return 50
            else:
                return 0
            

    def get_available_scores(self):

        available_scores = [-1 for i in range(11)]
        available_categories = self.state.board.get_available_categories()
        
        for i in available_categories:
            available_scores[i] = self.calculate_category_score(i)

        return available_scores
        

    def step(self, action):

        if (action.type == "roll"):

            old_state = deepcopy(self.state)
            
            self.state.dice.roll(action.lockList)
            self.state.numRolls += 1
            
            self.gameLogger.log_roll(old_state, action, self.state, self.get_available_scores(), old_state.board.get_available_categories())

            self.state.observation_space = self.get_observation_space()
            
            terminated = False

        elif (action.type == "pick"):

            old_state = deepcopy(self.state)

            score = self.get_available_scores()[action.category]

            self.state.board.pick_category(action.category, score)

            self.state.total_score += score
            self.state.numTurns += 1
            
            self.gameLogger.log_pick(old_state, action, self.state, score, self.rewardFunction(old_state, self.state, action), self.state.total_score)

            if len(self.state.board.get_available_categories()) != 0:

                available_scores = self.get_available_scores()
                available_categories = self.state.board.get_available_categories()
                
                self.state.numRolls = 1

                old_state = deepcopy(self.state)
                self.state.dice.roll()

                new_available_scores = self.get_available_scores()
    
                self.gameLogger.log_roll(old_state, action, self.state, new_available_scores, available_categories)

    
            self.state.is_game_over = (
                len(self.state.board.get_available_categories()) == 0
            )

            self.state.observation_space = self.get_observation_space()

            terminated = self.state.is_game_over
            
        reward = self.rewardFunction(old_state, self.state, action)
        
        truncated = False

        info = None

        return self.state, reward, terminated, truncated, info

            
            