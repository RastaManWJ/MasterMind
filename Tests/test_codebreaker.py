import unittest

from codebreaker import CodeBreaker


class TestCodeBreaker(unittest.TestCase):
    """Class to check a CodeBreaker implementation."""

    def test_CodeBreakerGetsPoint(self):
        """Check if CodeBreaker gets points."""
        player = CodeBreaker()
        self.assertEqual(player.points, 0)
        player.add_point()
        self.assertEqual(player.points, 1)

    def test_CodeBreakersPointsReset(self):
        """Check if CodeBreaker's points reset."""
        player = CodeBreaker()
        player.add_point()
        player.add_point()
        self.assertEqual(player.points, 2)
        player.reset_points()
        self.assertEqual(player.points, 0)

    def test_CodeBreakerMakesFullCode(self):
        """Check if CodeBreaker's guess is not None."""
        player = CodeBreaker()
        player.change_first_color(0)
        player.change_second_color(1)
        player.change_third_color(2)
        player.change_fourth_color(3)
        self.assertEqual(player.guess, [0, 1, 2, 3])
        self.assertTrue(player.confirm_guess())

    def test_CodeBreakerMakesCondemnedCode(self):
        """Check if CodeBreaker's guess is not complete."""
        player = CodeBreaker()
        player.change_third_color(0)
        player.change_fourth_color(2)
        self.assertEqual(player.guess, [None, None, 0, 2])
        self.assertFalse(player.confirm_guess())

    def test_CodeBreakerChangesColorOfHisGuess(self):
        """Check if CodeBreaker can change it's choice."""
        player = CodeBreaker()
        player.change_first_color(0)
        player.change_second_color(0)
        player.change_third_color(0)
        player.change_fourth_color(0)
        player.change_first_color(2)
        player.change_fourth_color(2)
        self.assertEqual(player.guess, [2, 0, 0, 2])

    def test_CodeBreakerResetsGuess(self):
        """Check if CodeBreaker guess can be reset."""
        player = CodeBreaker()
        player.change_first_color(1)
        player.change_second_color(2)
        player.change_third_color(3)
        player.change_fourth_color(4)
        self.assertEqual(player.guess, [1, 2, 3, 4])
        player.reset_guess()
        self.assertEqual(player.guess, [None, None, None, None])

