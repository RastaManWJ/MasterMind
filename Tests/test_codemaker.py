import unittest

from codemaker import Codemaker


class TestCodemaker(unittest.TestCase):
    def test_CodemakerInit(self):
        ai = Codemaker()
        self.assertEqual(ai.code, [None]*4)

    def test_CodemakerMadeAPatternOfFourCodePegs(self):
        ai = Codemaker()
        self.assertEqual(ai.code, [None]*4)
        ai.draw_code()
        self.assertNotEqual(ai.code, [None]*4)

    def test_CodemakerProvidedFeedbackOfAllWrongPegs(self):
        ai = Codemaker()
        ai.code = [0, 1, 2, 3]
        guess = [4, 4, 4, 4]
        feedback = ai.provide_feedback(guess)
        self.assertEqual([0, 0, 0, 0], feedback)

    def test_CodemakerProvidedFeedbackOfTwoCorrectIdealPlacements(self):
        ai = Codemaker()
        ai.code = [0, 1, 2, 3]
        guess = [0, 1, 4, 4]
        feedback = ai.provide_feedback(guess)
        self.assertEqual([2, 2, 0, 0], feedback)

    def test_CodemakerProvidedFeedbackOfTwoMatchingButWrongPlacedColors(self):
        ai = Codemaker()
        ai.code = [0, 1, 2, 3]
        guess = [1, 0, 4, 4]
        feedback = ai.provide_feedback(guess)
        self.assertEqual([1, 1, 0, 0], feedback)

    def test_CodemakerProvidedFeedbackOfTwoCorrectAndOneWrongPlacedColors(self):
        ai = Codemaker()
        ai.code = [0, 1, 2, 3]
        guess = [1, 4, 2, 3]
        feedback = ai.provide_feedback(guess)
        self.assertEqual([2, 2, 1, 0], feedback)

    def test_FeedbackResets(self):
        ai = Codemaker()
        ai.code = [0, 1, 2, 3]
        guess = [1, 4, 2, 3]
        feedback = ai.provide_feedback(guess)
        self.assertEqual([2, 2, 1, 0], feedback)
        ai.reset_feedback_pegs()
        self.assertEqual(ai.key_pegs, [0]*4)
        self.assertEqual(ai.key_peg_amount, 0)