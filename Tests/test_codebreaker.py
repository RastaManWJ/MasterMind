import unittest

from codebreaker import Codebreaker


class TestCodebreaker(unittest.TestCase):
    def test_CodebreakerGetsPoint(self):
        player = Codebreaker()
        self.assertEqual(player.points, 0)
        player.add_point()
        self.assertEqual(player.points, 1)

    def test_CodebreakersPointsReset(self):
        player = Codebreaker()
        player.add_point()
        player.add_point()
        self.assertEqual(player.points, 2)
        player.reset_points()
        self.assertEqual(player.points, 0)

    def test_CodebreakerAttemptsToGuessTheCode(self):
        player = Codebreaker()
        player.prepare_guess(0, 0, 0, 0)
        self.assertEqual(player.guess, [0, 0, 0, 0])
        player.prepare_guess(1, 5, 3, 2)
        self.assertEqual(player.guess, [1, 5, 3, 2])