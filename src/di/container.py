from datasource.storage import Storage
from datasource.mapper.game_mapper import GameMapper
from domain.service.impl import GameServiceImpl
from datasource.repository.game_repository import GameRepository

class Container:
    
    def __init__(self):
        self._storage = Storage()
        self._mapper = GameMapper()
        self._repository = GameRepository(self._storage, self._mapper)
        self._service = GameServiceImpl(self._repository)

    def get_service(self):
        return self._service