
class GameRepository:
    
    def __init__(self, storage, mapper):
        self.storage = storage
        self.mapper = mapper 

    def save(self, game):
        game_ds = self.mapper.to_datasource(game)
        self.storage.save(game_ds.uuid, game_ds)

    def load(self, game_uuid):
        game_ds = self.storage.get(game_uuid)
        if game_ds is None:
            return None
        return self.mapper.to_domain(game_ds)