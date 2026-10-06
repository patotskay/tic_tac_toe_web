import copy
from domain.model.game import Game
from web.model.game import GameWeb
from web.model.field import FieldWeb
class GameWebMapper:

    def to_domain(self, game_web):
        game = Game(game_uuid=game_web.uuid)
        game.field.field = copy.deepcopy(game_web.field.field)
        return game

    def to_web(self, game):
        field_web = FieldWeb(copy.deepcopy(game.field.field))
        game_web = GameWeb(game.uuid, field_web)
        return game_web