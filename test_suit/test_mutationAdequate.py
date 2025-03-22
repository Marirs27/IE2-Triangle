import unittest
from isTriangle import Triangle

class TestMutationAdequacy(unittest.TestCase):

    def testEquilateral(self):
        self.assertEqual(Triangle.classify(8, 8, 8), Triangle.Type.EQUILATERAL)

    def testScalene(self):
        self.assertEqual(Triangle.classify(11, 13, 9), Triangle.Type.SCALENE)

    def testIsosceles(self):
        self.assertEqual(Triangle.classify(8, 8, 5), Triangle.Type.ISOSCELES)

    def testInvalidZero(self):
        self.assertEqual(Triangle.classify(0, 6, 6), Triangle.Type.INVALID)

    def testInvalidNegative(self):
        self.assertEqual(Triangle.classify(-1, 7, 7), Triangle.Type.INVALID)

    def testInvalidInequality1(self):
        self.assertEqual(Triangle.classify(2, 2, 5), Triangle.Type.INVALID)

    def testInvalidInequality2(self):
        self.assertEqual(Triangle.classify(12, 4, 5), Triangle.Type.INVALID)

    def testBoundaryCaseInequality(self):
        self.assertEqual(Triangle.classify(6, 6, 12), Triangle.Type.INVALID)  # Triangle rule just fails

    def testBoundaryCaseValid(self):
        self.assertEqual(Triangle.classify(6, 6, 11), Triangle.Type.ISOSCELES)  # Triangle rule just passes

    def testOffByOne(self):
        self.assertEqual(Triangle.classify(5, 5, 9), Triangle.Type.ISOSCELES)  # Corrected expectation

    def testSwappedInputs(self):
        self.assertEqual(Triangle.classify(7, 5, 5), Triangle.Type.ISOSCELES)  # Checks handling of different orders

    def testLargeValidTriangle(self):
        self.assertEqual(Triangle.classify(1000000, 1000000, 1000000), Triangle.Type.EQUILATERAL)  # Stress test

if __name__ == '__main__':
    unittest.main()
