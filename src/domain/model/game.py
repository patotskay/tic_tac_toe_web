import uuid
from domain.model.field import Field

class Game:

    def __init__(self, game_uuid=None):
        self.field = Field()
        if game_uuid == None:
            self.uuid = str(uuid.uuid4())
        else:
            self.uuid = game_uuid
