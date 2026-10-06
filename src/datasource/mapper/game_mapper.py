import copy
from domain.model.game import Game
from datasource.model.game import GameDS
from datasource.model.field import FieldDS

class GameMapper:

    def to_datasource(self, game):
        field_ds = FieldDS(copy.deepcopy(game.field.field))
        game_ds = GameDS(game.uuid, field_ds)
        return game_ds

    def to_domain(self, game_ds):
        game = Game(game_uuid=game_ds.uuid)
        game.field.field = copy.deepcopy(game_ds.field.field)
        return game