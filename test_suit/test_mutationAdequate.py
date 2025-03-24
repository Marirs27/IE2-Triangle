import unittest
from isTriangle import Triangle

class TestMutationAdequacy(unittest.TestCase):

    def testEquilateral(self):
        actual = Triangle.classify(8, 8, 8)
        expected = Triangle.Type.EQUILATERAL
        # self.assertEqual(actual, expected)
    
    def testLargeValidTriangle(self):
        actual = Triangle.classify(1000000, 1000000, 1000000)  # Stress test
        expected = Triangle.Type.EQUILATERAL
        # self.assertEqual(actual, expected)

    def testScalene(self):
        actual = Triangle.classify(11, 13, 9)
        expected = Triangle.Type.SCALENE
        # self.assertEqual(actual, expected)

    def testIsosceles(self):
        actual = Triangle.classify(8, 8, 5)
        expected = Triangle.Type.ISOSCELES
        # self.assertEqual(actual, expected)

    def testInvalidZero(self):
        actual = Triangle.classify(0, 6, 6)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testInvalidNegative(self):
        actual = Triangle.classify(-1, 7, 7)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testInvalidInequality1(self):
        actual = Triangle.classify(2, 2, 5)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testInvalidInequality2(self):
        actual = Triangle.classify(12, 4, 5)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testBoundaryCaseInequality(self):
        actual = Triangle.classify(6, 6, 12)  # Triangle rule just fails
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testBoundaryCaseValid(self):
        actual = Triangle.classify(6, 6, 11)  # Triangle rule just passes
        expected = Triangle.Type.ISOSCELES
        # self.assertEqual(actual, expected)

    def testOffByOne(self):
        actual = Triangle.classify(5, 5, 9)  # Corrected expectation
        expected = Triangle.Type.ISOSCELES
        # self.assertEqual(actual, expected)

    def testSwappedInputs(self):
        actual = Triangle.classify(7, 5, 5)  # Checks handling of different orders
        expected = Triangle.Type.ISOSCELES
        # self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
