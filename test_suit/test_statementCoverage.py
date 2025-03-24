import unittest
from isTriangle import Triangle

class TestStatementCoverage(unittest.TestCase):

    # Valid Triangles
    def testEquilateral(self):
        actual = Triangle.classify(16, 16, 16)
        expected = Triangle.Type.EQUILATERAL
        # self.assertEqual(actual, expected)

    def testScalene(self):
        actual = Triangle.classify(7, 10, 5)
        expected = Triangle.Type.SCALENE
        # self.assertEqual(actual, expected)

    def testIsosceles1(self):
        actual = Triangle.classify(26, 26, 24)
        expected = Triangle.Type.ISOSCELES
        # self.assertEqual(actual, expected)

    def testIsosceles2(self):
        actual = Triangle.classify(15, 13, 15)
        expected = Triangle.Type.ISOSCELES
        # self.assertEqual(actual, expected)

    # Invalid Triangles
    def testInvalidZero(self):
        actual = Triangle.classify(0, 51, 51)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testInvalidNegative(self):
        actual = Triangle.classify(-10, 4, 5)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testInvalidInequality1(self):
        actual = Triangle.classify(1, 2, 3)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testInvalidInequality2(self):
        actual = Triangle.classify(50, 10, 10)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testInvalidInequality3(self):
        actual = Triangle.classify(101, 100, 1)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testInvalidInequality4(self):
        actual = Triangle.classify(6, 10, 3)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    # Edge and Boundary Cases
    def testBoundaryCase(self):
        actual = Triangle.classify(10, 10, 20)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testStressTestScalene(self):
        actual = Triangle.classify(999999, 1000000, 1000001)
        expected = Triangle.Type.SCALENE
        # self.assertEqual(actual, expected)

    def testStressTestEquilateral(self):
        actual = Triangle.classify(1010001, 1010001, 1010001)
        expected = Triangle.Type.EQUILATERAL
        # self.assertEqual(actual, expected)

    def testStressTestIsosceles(self):
        actual = Triangle.classify(1010000, 1010001, 1010001)
        expected = Triangle.Type.ISOSCELES
        # self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main()