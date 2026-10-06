from domain.service.interface import GameService

class GameServiceImpl(GameService):

    def __init__(self, repository):
        self.repository = repository

    def make_move(self, game_uuid, new_field):
        game = self.repository.load(game_uuid)
        if game is None:
            raise ValueError('Игра с таким UUID не найдена')

        if not self.validate(game.field.field, new_field):
            raise ValueError('Невалидный ход')

        game.field.field = new_field

        if self.check_game_over(game.field.field) is not None:
            self.repository.save(game)
            return game

        move = self.get_next_move(game)
        if move is None:
            raise ValueError('Нет доступных ходов')

        i, j = move
        game.field.field[i][j] = 1

        self.repository.save(game)

        return game

    def validation(self, old_field, cur_field):
        diff = []
        for i in range(3):
            for j in range(3):
                if old_field[i][j] != cur_field[i][j]:
                    diff.append(old_field[i][j], cur_field[i][j])
        if len(diff) != 1:
            return False
        
        old, cur = diff[0]
        return old == 0 and cur == 2
            
    def check_game_over(self, field):
        winning_combinations = (((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)), #диагонали
                                ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)), #cтолбики
                                ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)) #строки
        )

        for wc in winning_combinations:
            if all(field[i][j] == 2 for i, j in wc):
                return -1
            elif all(field[i][j] == 1 for i, j in wc):
                return 1
        
        for row in field:
            if 0 in row:
                return None
        
        return 0
                

    def get_next_move(self, game):
        best_score = -float('inf')
        best_move = None

        for i in range(3):
            for j in range(3):
                if game.field.field[i][j] == 0:
                    game.field.field[i][j] = 1
                    score = self._minimax(game.field.field, depth=0, is_maximizing=False)
                    game.field.field[i][j] = 0

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move

    def _minimax(self, field, depth, is_maximizing):
        result = self.check_game_over(field)
        if result:
            return result
        
        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if field[i][j] == 0:
                        field[i][j] = 1
                        score = self._minimax(field, depth + 1, False)
                        field[i][j] = 0
                        best_score = max(score, best_score)

            return best_score

        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if field[i][j] == 0:
                        field[i][j] = 2
                        score = self._minimax(field, depth + 1, True)
                        field[i][j] = 0
                        best_score = min(score, best_score)

            return best_score

    