import time
from player import Human, RandomCompPlayer, SmartCompPlayer


class TicTacToe:

    def __init__(self):
        self.board = [' ' for _ in range(9)]  # single list to represent a 3x3 game board
        self.current_winner = None  # keeping track of a winner

    def print_board(self):
        # this gets the 3 rows
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def board_nums():
        # 0 | 1 | 2 etc. (tells us what number goes to what box)
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_sq(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check if there are 3 in a row ANYWHERE
        # first check rows
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check columns
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        if square % 2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]]  # top left to bottom right diagonal
            if all([spot == letter for spot in diag1]):
                return True
            diag2 = [self.board[i] for i in [2, 4, 6]]  # top right to bottom left diagonal
            if all([spot == letter for spot in diag2]):
                return True

        # if all these fail:
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.board_nums()
    letter = 'X'  # starting letter

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' is the winner!!')
                return letter
            # alternate letters after the move
            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'

        if print_game:
            time.sleep(1)

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = Human('X')
    # o_player = RandomCompPlayer('O')
    o_player = SmartCompPlayer('O')  # smart moves by the computer, cannot win at all
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)


# MAKE THE COMPUTER PLAY AGAINST ITSELF:
"""
if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(100):
        x_player = RandomCompPlayer('X')
        o_player = SmartCompPlayer('O')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1

    print(f'After 100 iterations, we see {x_wins} X wins, {o_wins} O wins, and {ties} number of ties!')
"""
