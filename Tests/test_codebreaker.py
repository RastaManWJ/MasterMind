import unittest


class TestCodebreaker(unittest.TestCase):
    def test_CodebreakerAttemptsToGuessTheCode(self):
        self.assertTrue(GuessAttemptConfirmed())