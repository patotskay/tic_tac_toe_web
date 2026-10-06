import threading

class Storage:

    def __init__(self):
        self._storage = {}
        self._lock = threading.Lock()

    def save(self, game_uuid, game_data):
        with self._lock:
            self._storage[game_uuid] = game_data 

    def get(self, game_uuid):
        with self._lock:
            return self._storage[game_uuid]