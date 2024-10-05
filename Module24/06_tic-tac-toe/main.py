# TODO здесь писать код
from ast import Index
class Cell:
    #  Клетка, у которой есть значения
    #   - занята она или нет
    #   - номер клетки
    def __init__(self, num, occupy = False):
        self.num = num
        self.occupy = occupy
        self.sym = ' '

class Board:
    #  Класс поля, который создаёт у себя экземпляры клетки
    def __init__(self):
        self.cells = [Cell(num) for num in range(9)]

    def board_vision(self):
        counter = 0
        for i in range(3):
            for j in range(3):
                print(self.cells[counter].sym, end = ' ')
                counter += 1
            print()

    def full_or_not(self):
        return all([cell.occupy for cell in self.cells])


class Player:
    def __init__(self, name, sym, num_cell = 0):
    #  У игрока может быть
    #   - имя
    #   - на какую клетку ходит
        self.name = name
        self.num_cell = num_cell
        self.sym = sym

class Game:
    # класс «Игры» содержит атрибуты:
    # состояние игры,
    # игроки,
    # поле.
    # А также методы:
    # Метод запуска одного хода игры. Получает одного из игроков, запрашивает у игрока номер клетки, изменяет поле, проверяет, выиграл ли игрок. Если игрок победил, возвращает True, иначе False.
    # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который завершается победой одного из игроков или ничьей. Если игра завершена, метод возвращает True, иначе False.
    # Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой игры, хотят ли игроки продолжать играть. После каждой игры выводится текущий счёт игроков.
    def __init__(self, players, board = Board(), game_condition = False):
        self.game_condition = game_condition
        self.players = players
        self.board = board
        pass

    def one_move(self, player):
        try:
            num_cell = int(input(f'{player.name}, введите номер клетки(0-8): '))
            player.num_cell = num_cell

            if self.board.cells[num_cell].occupy == False:
                self.board.cells[num_cell].occupy = True
                self.board.cells[num_cell].sym = player.sym
            else:
                print('эта клетка уже занята, пожалуйтса, выберите другую клетку')
                self.one_move(player)
        except (IndexError,ValueError):
            print('Ошибка, введите число от 0 до 8')
            self.one_move(player)

        if self.board.cells[0].sym == player.sym and self.board.cells[1].sym == player.sym  and self.board.cells[2].sym == player.sym:
            return True
        elif self.board.cells[3].sym == player.sym and self.board.cells[4].sym == player.sym  and self.board.cells[5].sym == player.sym:
            return True
        elif self.board.cells[6].sym == player.sym and self.board.cells[7].sym == player.sym  and self.board.cells[8].sym == player.sym:
            return True
        elif self.board.cells[0].sym == player.sym and self.board.cells[3].sym == player.sym  and self.board.cells[6].sym == player.sym:
            return True
        elif self.board.cells[1].sym == player.sym and self.board.cells[4].sym == player.sym  and self.board.cells[7].sym == player.sym:
            return True
        elif self.board.cells[2].sym == player.sym and self.board.cells[5].sym == player.sym  and self.board.cells[8].sym == player.sym:
            return True
        elif self.board.cells[0].sym == player.sym and self.board.cells[4].sym == player.sym  and self.board.cells[8].sym == player.sym:
            return True
        elif self.board.cells[2].sym == player.sym and self.board.cells[4].sym == player.sym  and self.board.cells[6].sym == player.sym:
            return True
        else:
            return False

    def one_game(self):
        for cell in self.board.cells:
            cell.occupy = False
            cell.sym = ' '
        while True:
            if self.board.full_or_not():
                print('Все клетки заняты! Ничья')
                return 0
                break
            if self.one_move(self.players[0]):
                print(f'Победу одержал {self.players[0].name}')
                self.board.board_vision()
                return 1
                break
            self.board.board_vision()
            if self.board.full_or_not():
                print('Все клетки заняты! Ничья')
                return 0
                break
            elif self.one_move(self.players[1]):
                print(f'Победу одержал {self.players[1].name}')
                self.board.board_vision()
                return 2
                break
            self.board.board_vision()

    def main_game(self):
        win_1 = 0
        win_2 = 0
        while True:
            num = self.one_game()
            if num == 1:
                win_1 += 1
            elif num == 2:
                win_2 += 1
            print(f'Желаете продолжить игру? Текущий счет:\n'
                  f'{self.players[0].name} = {win_1}, {self.players[1].name} = {win_2}')

            answer = input('Ответ(да или нет): ')
            while answer.lower() != 'да' and answer.lower() != 'нет':
                print('Некорректный ответ. Введите да или нет')
                answer = input('Ответ(да или нет): ')
            if answer.lower() == 'нет':
                break


game = Game(players = [Player('Вася', 'X'), Player('Саша', '0')])
game.main_game()