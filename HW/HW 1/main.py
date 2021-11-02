from enum import IntEnum
import numpy as np


class Player(IntEnum):
    first = 0
    second = 1
    num_players = 2


class TicTacGame:

    def __init__(self):

        self.FIELD_SIZE = 3

        self._board_player = list()

        self._board_player = np.zeros((
            Player.num_players, self.FIELD_SIZE, self.FIELD_SIZE), dtype=bool)

        self._current_player = Player.second
        self._current_move = None
        self._num_current_move = 0

    def start_game(self):

        player_names = list()

        print("The name of the first player?")
        player_names.append(input())

        print("The name of the second player?")
        player_names.append(input())

        while not self.check_winner():

            if self._num_current_move == self.FIELD_SIZE ** 2:
                print("Draw!")
                break

            if self._current_player == Player.first:
                self._current_player = Player.second
            else:
                self._current_player = Player.first

            self.show_board()

            # TODO
            print(f"Your turn {player_names[self._current_player]}")
            print("Select a cell")
            self._current_move = input()

            while not self.validate_input(self._current_move):
                print("Try again")
                print(f"Your turn {player_names[self._current_player]}")
                print("Select a cell")
                self._current_move = input()

            self._current_move = int(self._current_move)
            self._board_player[self._current_player][self._current_move
                                                     // self.FIELD_SIZE][
                self._current_move % self.FIELD_SIZE] = True

            self._num_current_move += 1

        else:
            self.show_board()
            print(f"You win {player_names[self._current_player]}")

    def show_board(self):
        for i in range(self.FIELD_SIZE):
            for j in range(self.FIELD_SIZE):
                if j != 0 and j != self.FIELD_SIZE:
                    print('|', end='')
                if self._board_player[Player.first][i][j]:
                    print('x', end='')
                elif self._board_player[Player.second][i][j]:
                    print('o', end='')
                else:
                    print(i * self.FIELD_SIZE + j, end='')
            print()
            for j in range(self.FIELD_SIZE):
                if i != self.FIELD_SIZE - 1 and i != self.FIELD_SIZE:
                    print('— ', end='')
            print()

    def validate_input(self, inp):

        self._current_move = inp

        # TODO

        return self._current_move.isdigit() and not \
            self.FIELD_SIZE ** 2 - 1 < int(self._current_move) and not \
            int(self._current_move) < 0 and not \
            self._board_player[Player.first][
            int(self._current_move) // self.FIELD_SIZE][
            int(self._current_move) % self.FIELD_SIZE] and not \
            self._board_player[Player.second][
            int(self._current_move) // self.FIELD_SIZE][
            int(self._current_move) % self.FIELD_SIZE]

    def check_winner(self):

        if self._num_current_move < 2 * self.FIELD_SIZE - 1:
            return False

        is_win_main_diag = False
        if self._current_move % self.FIELD_SIZE == \
                self._current_move // self.FIELD_SIZE:
            # main diagonal
            is_win_main_diag = True
            for i in range(self.FIELD_SIZE):
                is_win_main_diag *= \
                    self._board_player[self._current_player][i][i]

        is_win_side_diagonal = False
        if self._current_move % self.FIELD_SIZE == \
                self.FIELD_SIZE - self._current_move // self.FIELD_SIZE - 1:
            # side diagonal
            is_win_side_diagonal = True
            for i in range(self.FIELD_SIZE):
                is_win_side_diagonal *= \
                    self._board_player[self._current_player][i][
                        self.FIELD_SIZE - i - 1]

        is_win_horizon = True
        is_win_vertical = True
        for i in range(self.FIELD_SIZE):
            is_win_vertical *= \
                self._board_player[self._current_player][i][
                    self._current_move % self.FIELD_SIZE]
            is_win_horizon *= \
                self._board_player[self._current_player][self._current_move
                                                         // self.FIELD_SIZE][i]

        return bool(is_win_main_diag + is_win_side_diagonal
                    + is_win_horizon + is_win_vertical)


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
