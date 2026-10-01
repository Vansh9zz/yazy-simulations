from abc import ABC, abstractmethod

class Player(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def act(self, env):
        pass