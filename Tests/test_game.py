import unittest


class TestGame(unittest.TestCase):
    def test_CodebreakerWins(self):
        self.assertTrue(isCodeBroken())

    def test_CodemakerWins(self):
        self.assertFalse(isCodeBroken())