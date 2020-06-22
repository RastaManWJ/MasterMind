import unittest

from codemaker import CodeMaker


class TestCodeMaker(unittest.TestCase):
    """Class to check CodeMaker implementation."""
    
    def test_CodeMakerInit(self):
        """Check if CodeMaker initialize with blank code."""
        ai = CodeMaker()
        self.assertEqual(ai.code, [None]*4)

    def test_CodeMakerMadeAPatternOfFourCodePegs(self):
        """Check if CodeMaker makes code."""
        ai = CodeMaker()
        self.assertEqual(ai.code, [None]*4)
        ai.draw_code()
        self.assertNotEqual(ai.code, [None]*4)

    def test_CodeMakerProvidedFeedbackOfAllWrongPegs(self):
        """Check if CodeMaker provides feedback of whole wrong guess."""
        ai = CodeMaker()
        ai.code = [0, 1, 2, 3]
        guess = [4, 4, 4, 4]
        feedback = ai.provide_feedback(guess)
        self.assertEqual([0, 0, 0, 0], feedback)

    def test_CodeMakerProvidedFeedbackOfTwoCorrectIdealPlacements(self):
        """Check if CodeMaker provides feedback of 2 correct pegs."""
        ai = CodeMaker()
        ai.code = [0, 1, 2, 3]
        guess = [0, 1, 4, 4]
        feedback = ai.provide_feedback(guess)
        self.assertEqual([2, 2, 0, 0], feedback)

    def test_CodeMakerProvidedFeedbackOfTwoMatchingButWrongPlacedColors(self):
        """Check if CodeMaker provides feedback of 2 correct pegs in wrong place."""
        ai = CodeMaker()
        ai.code = [0, 1, 2, 3]
        guess = [1, 0, 4, 4]
        feedback = ai.provide_feedback(guess)
        self.assertEqual([1, 1, 0, 0], feedback)

    def test_CodeMakerProvidedFeedbackOfTwoCorrectAndOneWrongPlacedColors(self):
        """Check if CodeMaker provides feedback of various combination of correct pegs."""
        ai = CodeMaker()
        ai.code = [0, 1, 2, 3]
        guess = [1, 4, 2, 3]
        feedback = ai.provide_feedback(guess)
        self.assertEqual([2, 2, 1, 0], feedback)
        self.assertEqual(3, ai.key_peg_amount)

    def test_CodeMakerProvidedFeedbackOfAllCorrectlyPlacedPegs(self):
        """Check if CodeMaker provides feedback of all pegs in the correct place."""
        ai = CodeMaker()
        ai.code = [0, 1, 2, 3]
        guess = [0, 1, 2, 3]
        feedback = ai.provide_feedback(guess)
        self.assertEqual([2, 2, 2, 2], feedback)

    def test_CodeMakerProvidedFeedbackOfAllWrongPlacedColors(self):
        """Check if CodeMaker provides feedback of all pegs in wrong place."""
        ai = CodeMaker()
        ai.code = [0, 1, 2, 3]
        guess = [3, 2, 1, 0]
        feedback = ai.provide_feedback(guess)
        self.assertEqual([1, 1, 1, 1], feedback)

    def test_FeedbackResets(self):
        """"Check if feedback can be reset."""
        ai = CodeMaker()
        ai.code = [0, 1, 2, 3]
        guess = [1, 4, 2, 3]
        feedback = ai.provide_feedback(guess)
        self.assertEqual([2, 2, 1, 0], feedback)
        ai.reset_feedback_pegs()
        self.assertEqual(ai.key_pegs, [0]*4)
        self.assertEqual(ai.key_peg_amount, 0)