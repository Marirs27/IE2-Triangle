import unittest
from isTriangle import Triangle

class TestStatementCoverage(unittest.TestCase):

    # Valid Statements
    def testEquilateral(self):
        self.assertEqual(Triangle.classify(6, 6, 6), Triangle.Type.EQUILATERAL)

    def testScalene(self):
        self.assertEqual(Triangle.classify(7, 10, 5), Triangle.Type.SCALENE)

    def testIsosceles(self):
        self.assertEqual(Triangle.classify(6, 6, 4), Triangle.Type.ISOSCELES)

    # Invalid Statements
    def testInvalidZero(self):
        self.assertEqual(Triangle.classify(0, 5, 5), Triangle.Type.INVALID)

    def testInvalidNegative(self):
        self.assertEqual(Triangle.classify(-3, 4, 5), Triangle.Type.INVALID)

    def testInvalidInequality1(self):
        self.assertEqual(Triangle.classify(1, 2, 3), Triangle.Type.INVALID)

    def testInvalidInequality2(self):
        self.assertEqual(Triangle.classify(5, 1, 1), Triangle.Type.INVALID)  # Edge case  

    # Stress Test
    def stressTest(self):
        self.assertEqual(Triangle.classify(100000, 100000, 100000), Triangle.Type.EQUILATERAL)

if __name__ == '__main__':
    unittest.main()