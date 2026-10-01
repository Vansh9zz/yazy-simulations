class GameLogger:

    def __init__(self, id = 0, player_type = "player"):

        self.player_type = player_type
        self.id = id
        self.turns = []

        self.total_score = 0
        self.category_scores = [0 for i in range(11)]
        
        self.total_reward = 0

        for i in range(11):
            d = {}
            d["turn"] = i + 1

            d["rolls"] = []

            d["category_picked"] = -1
            d["score_obtained"] = 0
            d["reward_obtained"] = 0
            d["running_score"] = 0

            self.turns.append(d)           

    def log_roll(self, old_state, action, new_state, available_scores, available_categories):
        d = {}
        d["roll"] = new_state.numRolls
        d["dice"] = new_state.dice.values.copy()
        
        d["available_scores"] = available_scores.copy()
        d["available_categories"] = available_categories.copy()

        d["lock_list"] = action.lockList.copy() if action.lockList else None

        self.turns[old_state.numTurns - 1]["rolls"].append(d)

    def log_initial_roll(self, state, available_scores, available_categories):
        d = {}
        d["roll"] = state.numRolls
        d["dice"] = state.dice.values.copy()
        
        d["available_scores"] = available_scores.copy()
        d["available_categories"] = available_categories.copy()

        d["lock_list"] = None


        self.turns[state.numTurns - 1]["rolls"].append(d)

    def log_pick(self, old_state, action, new_state, score_obtained, reward_obtained, running_score):

        d = self.turns[old_state.numTurns - 1]
        d["category_picked"] = action.category
        d["score_obtained"] = score_obtained
        d["reward_obtained"] = reward_obtained
        d["running_score"] = running_score

        self.category_scores[action.category] = score_obtained
        self.total_score += score_obtained
        self.total_reward += reward_obtained

    def get_summary(self):

        summary = {}

        summary["id"] = self.id
        summary["player_type"] = self.player_type
        summary["total_score"] = self.total_score
        summary["total_reward"] = self.total_reward

        for i in range(11):
            summary[f"score_{i}"] = self.category_scores[i]

        return summary
        
        