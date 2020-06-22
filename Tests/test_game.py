import unittest
from game import Game


class TestGame(unittest.TestCase):
    """Class to check game implementation."""

    def test_GameBoardInit(self):
        """Check if Game initialization performs correctly."""
        game = Game(12)
        self.assertEqual(game.rows, 12)
        self.assertEqual(game.current_row, 0)

    def test_CodebreakerWins(self):
        """Check if CodeBreaker can win."""
        game = Game(12)
        self.assertEqual(game.winner, '')
        game.game_ends('CodeBreaker')
        self.assertEqual(game.winner, 'CodeBreaker')

    def test_CodemakerWins(self):
        """Check if CodeMaker can win."""
        game = Game(12)
        self.assertEqual(game.winner, '')
        game.game_ends('CodeMaker')
        self.assertEqual(game.winner, 'CodeMaker')