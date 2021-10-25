import unittest
import numpy as np
from main import TicTacGame


class TestGame(unittest.TestCase):

    def setUp(self) -> None:
        self.game = TicTacGame()

        self.game_win_first_horizon = TicTacGame()
        self.game_win_first_horizon._board_player = np.zeros(
            (2, self.game_win_first_horizon.FIELD_SIZE, self.game_win_first_horizon.FIELD_SIZE), dtype=bool)
        self.game_win_first_horizon._board_player = [[[1, 1, 1],
                                                      [0, 0, 0],
                                                      [0, 0, 0]], [[0, 0, 0],
                                                                   [0, 0, 0],
                                                                   [0, 0, 0]]]
        self.game_win_first_horizon._num_current_move = 7
        self.game_win_first_horizon._current_move = 0
        self.game_win_first_horizon._current_player = 0

        self.game_win_second_main_diagonal = TicTacGame()
        self.game_win_second_main_diagonal._board_player = np.zeros(
            (2, self.game_win_second_main_diagonal.FIELD_SIZE, self.game_win_second_main_diagonal.FIELD_SIZE),
            dtype=bool)
        self.game_win_second_main_diagonal._board_player = [[[0, 0, 1],
                                                             [0, 0, 0],
                                                             [0, 0, 0]], [[1, 0, 0],
                                                                          [0, 1, 0],
                                                                          [0, 0, 1]]]
        self.game_win_second_main_diagonal._num_current_move = 7
        self.game_win_second_main_diagonal._current_move = 0
        self.game_win_second_main_diagonal._current_player = 1
        self.game_draw = TicTacGame()
        self.game_draw._board_player = np.zeros(
            (2, self.game_draw.FIELD_SIZE, self.game_draw.FIELD_SIZE), dtype=bool)

        self.game_win_second_side_diagonal = TicTacGame()
        self.game_win_second_side_diagonal._board_player = np.zeros(
            (2, self.game_win_second_side_diagonal.FIELD_SIZE, self.game_win_second_side_diagonal.FIELD_SIZE),
            dtype=bool)
        self.game_win_second_side_diagonal._board_player = [[[0, 0, 1],
                                                             [0, 0, 0],
                                                             [0, 0, 0]], [[0, 0, 1],
                                                                          [0, 1, 0],
                                                                          [1, 0, 0]]]
        self.game_win_second_side_diagonal._num_current_move = 7
        self.game_win_second_side_diagonal._current_move = 2
        self.game_win_second_side_diagonal._current_player = 1
        self.game_draw = TicTacGame()
        self.game_draw._board_player = np.zeros(
            (2, self.game_draw.FIELD_SIZE, self.game_draw.FIELD_SIZE), dtype=bool)

    def test_valid_input(self):
        self.assertTrue(self.game.validate_input('0'))
        self.assertTrue(self.game.validate_input('8'))

    def test_invalid_input(self):
        self.assertFalse(self.game.validate_input('9'))
        self.assertFalse(self.game.validate_input('-1'))
        self.assertFalse(self.game.validate_input("qwerty"))

    def test_check_winner(self):
        self.assertTrue(self.game_win_first_horizon.check_winner())
        self.assertTrue(self.game_win_second_main_diagonal.check_winner())
        self.assertTrue(self.game_win_second_side_diagonal.check_winner())

    def tearDown(self) -> None:
        print("All right!")


if __name__ == '__main__':
    unittest.main()
