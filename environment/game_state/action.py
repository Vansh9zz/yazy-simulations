class Action:

    def __init__(self, type, lockList = None, category = None):

        self.type = type

        if (lockList and category):
            raise ValueError
            
        self.lockList = lockList
        self.category = category