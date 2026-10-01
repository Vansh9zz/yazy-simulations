class Board:
    def __init__(self):
        self.scores = [0 for i in range(11)]
        self.taken = [False for i in range(11)]
        self.available_categories = [i for i in range(11)]

    def pick_category(self, idx, score):
        self.scores[idx] = score
        self.taken[idx] = True
        self.available_categories.remove(idx)

    def get_available_categories(self):
        return self.available_categories