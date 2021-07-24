import unittest
import sys
from shishua import SHISHUA

class SHISHUATest(unittest.TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, SHISHUA, 0.5)

        # Must not raise:
        SHISHUA()
        SHISHUA(0)
        SHISHUA(12345678901234567890)
        SHISHUA(-1)
        SHISHUA([0, 1, 2, 3, 4])
        SHISHUA([-1, 12345678901234567890])
        SHISHUA("")

def testsuite():
    suite = unittest.TestSuite()
    cases = [SHISHUATest]
    for c in cases:
        suite.addTests(unittest.makeSuite(c))
    return suite

if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(testsuite())
    sys.exit(not result.wasSuccessful())
