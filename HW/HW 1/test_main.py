import unittest
import numpy as np
from main import TicTacGame


class TestGame(unittest.TestCase):

    def setUp(self) -> None:
        self.game = TicTacGame()
        self.game_win_first_g = TicTacGame()
        self.game_win_first_g._board_player = np.zeros(
            (2, self.game_win_first_g.FIELD_SIZE, self.game_win_first_g.FIELD_SIZE), dtype=bool)
        self.game_win_first_g._board_player = [[[1, 1, 1],
                                                [0, 0, 0],
                                                [0, 0, 0]], [[0, 0, 0],
                                                             [0, 0, 0],
                                                             [0, 0, 0]]]
        self.game_win_first_g._num_current_move = 7
        self.game_win_first_g._current_move = 0
        self.game_win_first_g._current_player = 0
        self.game_win_second_d = TicTacGame()
        self.game_win_second_d._board_player = np.zeros(
            (2, self.game_win_second_d.FIELD_SIZE, self.game_win_second_d.FIELD_SIZE), dtype=bool)
        self.game_win_second_d._board_player = [[[0, 0, 1],
                                                 [0, 0, 0],
                                                 [0, 0, 0]], [[1, 0, 0],
                                                              [0, 1, 0],
                                                              [0, 0, 1]]]
        self.game_win_second_d._num_current_move = 7
        self.game_win_second_d._current_move = 0
        self.game_win_second_d._current_player = 1
        self.game_draw = TicTacGame()
        self.game_draw._board_player = np.zeros(
            (2, self.game_draw.FIELD_SIZE, self.game_draw.FIELD_SIZE), dtype=bool)
        self.game_draw._board_player = [[[0, 1, 1],
                                         [1, 1, 0],
                                         [0, 0, 1]], [[1, 0, 0],
                                                      [0, 0, 1],
                                                      [1, 1, 0]]]
        self.game_draw._num_current_move = self.game_draw.FIELD_SIZE ** 2
        self.game_draw._current_move = 0
        self.game_draw._current_player = 1

    def test_valid_input(self):
        self.assertTrue(self.game.validate_input('0'))
        self.assertTrue(self.game.validate_input('8'))

    def test_invalid_input(self):
        self.assertFalse(self.game.validate_input('9'))
        self.assertFalse(self.game.validate_input('-1'))
        self.assertFalse(self.game.validate_input("qwerty"))

    def test_check_winner(self):
        self.assertTrue(self.game_win_first_g.check_winner())
        self.assertTrue(self.game_win_second_d.check_winner())
        self.assertTrue(self.game_draw.check_winner())

    def tearDown(self) -> None:
        print("Test done!")


if __name__ == '__main__':
    unittest.main()
