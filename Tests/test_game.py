import unittest

from game import Game


class TestGame(unittest.TestCase):
    def test_GameBoardInit(self):
        game = Game(12)
        self.assertEqual(game.rows, 12)
        self.assertEqual(game.current_row, 0)

    def test_CodebreakerWins(self):
        game = Game(12)
        self.assertEqual(game.winner, '')
        game.game_ends('Codebreaker')
        self.assertEqual(game.winner, 'Codebreaker')

    def test_CodemakerWins(self):
        game = Game(12)
        self.assertEqual(game.winner, '')
        game.game_ends('Codemaker')
        self.assertEqual(game.winner, 'Codemaker')