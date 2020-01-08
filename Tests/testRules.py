import unittest


class TestRulesOfTheGame(unittest.TestCase):
    def test_CodemakerMadeAPatternOfFourCodePegs(self):
        self.assertTrue(MakeHiddenCode())

    def test_CodemakerProvidedFeedback(self):
        self.assertTrue(ProvideFeedback())

    def test_CodebreakerAttemptsToGuessTheCode(self):
        self.assertTrue(GuessAttemptConfirmed())

    def test_CodebreakerWins(self):
        self.assertTrue(isCodeBroken())

    def test_CodemakerWins(self):
        self.assertFalse(isCodeBroken())


if __name__ == '__main__':
    unittest.main()
