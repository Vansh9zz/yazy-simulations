import random

class Dice:
    def __init__(self):
        self.values = [0 for _ in range(5)]
        # self.locked = [False for _ in range(5)]

    def roll(self, lockList = None):

        if lockList:
            locked = lockList
        else:
            locked = []
            
        for i in range(5):
            if i not in locked:
                self.values[i] = random.randint(1,6)

        return self.values

    def sum(self):
        return sum(self.values)

    def frequency(self):

        map = [0 for i in range(6)]

        for i in range(5):
            map[self.values[i] - 1] += 1

        frequency = {idx : map[idx - 1] for idx in range(1,7)}
        return frequency

    def sorted(self):
        return sorted(self.values)

    def reset(self):
        self.values = [0 for i in range(5)]