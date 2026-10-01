def defaultReward(old_state, new_state, action):
    return new_state.total_score - old_state.total_score