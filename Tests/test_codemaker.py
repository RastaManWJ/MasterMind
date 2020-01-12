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

    def test_CodemakerProvidedFeedback(self):
        pass

