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

    def test_CodebreakerMakesFullCode(self):
        player = Codebreaker()
        player.change_first_color(0)
        player.change_second_color(1)
        player.change_third_color(2)
        player.change_fourth_color(3)
        self.assertEqual(player.guess, [0, 1, 2, 3])
        self.assertTrue(player.confirm_guess())

    def test_CodebreakerMakesCondemnedCode(self):
        player = Codebreaker()
        player.change_third_color(0)
        player.change_fourth_color(2)
        self.assertEqual(player.guess, [None, None, 0, 2])
        self.assertFalse(player.confirm_guess())

    def test_CodebreakerChangesColorOfHisGuess(self):
        player = Codebreaker()
        player.change_first_color(0)
        player.change_second_color(0)
        player.change_third_color(0)
        player.change_fourth_color(0)
        player.change_first_color(2)
        player.change_fourth_color(2)
        self.assertEqual(player.guess, [2, 0, 0, 2])

    def test_CodebreakerResetsGuess(self):
        player = Codebreaker()
        player.change_first_color(1)
        player.change_second_color(2)
        player.change_third_color(3)
        player.change_fourth_color(4)
        self.assertEqual(player.guess, [1, 2, 3, 4])
        player.reset_guess()
        self.assertEqual(player.guess, [None, None, None, None])

