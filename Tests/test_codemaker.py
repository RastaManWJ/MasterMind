import unittest


class TestCodemaker(unittest.TestCase):
    def test_CodemakerMadeAPatternOfFourCodePegs(self):
        self.assertTrue(MakeHiddenCode())

    def test_CodemakerProvidedFeedback(self):
        self.assertTrue(ProvideFeedback())



if __name__ == '__main__':
    unittest.main()
