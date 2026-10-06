from abc import ABC, abstractmethod

class GameService(ABC):

    @abstractmethod
    def get_next_move(self, game):
        pass

    @abstractmethod
    def validate(self, game):
        pass

    @abstractmethod
    def check_game_over(self, field):
        pass