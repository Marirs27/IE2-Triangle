import unittest
from isTriangle import Triangle

class TestStatementCoverage(unittest.TestCase):

    # Valid Triangles
    def testEquilateral(self):
        self.assertEqual(Triangle.classify(6, 6, 6), Triangle.Type.EQUILATERAL)

    def testScalene(self):
        self.assertEqual(Triangle.classify(7, 10, 5), Triangle.Type.SCALENE)

    def testIsosceles1(self):
        self.assertEqual(Triangle.classify(6, 6, 4), Triangle.Type.ISOSCELES)

    def testIsosceles2(self):
        self.assertEqual(Triangle.classify(5, 3, 5), Triangle.Type.ISOSCELES)  # Different order

    # Invalid Triangles
    def testInvalidZero(self):
        self.assertEqual(Triangle.classify(0, 5, 5), Triangle.Type.INVALID)

    def testInvalidNegative(self):
        self.assertEqual(Triangle.classify(-3, 4, 5), Triangle.Type.INVALID)

    def testInvalidInequality1(self):
        self.assertEqual(Triangle.classify(1, 2, 3), Triangle.Type.INVALID)

    def testInvalidInequality2(self):
        self.assertEqual(Triangle.classify(5, 1, 1), Triangle.Type.INVALID)

    def testInvalidInequality3(self):
        self.assertEqual(Triangle.classify(10, 5, 5), Triangle.Type.INVALID) 

    def testInvalidInequality4(self):
        self.assertEqual(Triangle.classify(6, 10, 3), Triangle.Type.INVALID) 

    # Edge and Boundary Cases
    def testBoundaryCase(self):
        self.assertEqual(Triangle.classify(5, 5, 10), Triangle.Type.INVALID) 

    def testStressTestScalene(self):
        self.assertEqual(Triangle.classify(999999, 1000000, 1000001), Triangle.Type.SCALENE) 

    def testStressTestEquilateral(self):
        self.assertEqual(Triangle.classify(1010001, 1010001, 1010001), Triangle.Type.EQUILATERAL) 
        
    def testStressTestIsosceles(self):
        self.assertEqual(Triangle.classify(1010000, 1010001, 1010001), Triangle.Type.ISOSCELES) 

if __name__ == '__main__':
    unittest.main()
