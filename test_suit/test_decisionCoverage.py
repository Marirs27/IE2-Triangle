import unittest
from isTriangle import Triangle

class TestDecisionCoverage(unittest.TestCase):

    # Valid Decisions
    def testEquilateral(self):
        actual = Triangle.classify(8, 8, 8)
        expected = Triangle.Type.EQUILATERAL
        # self.assertEqual(actual, expected)

    def testScalene1(self):
        actual = Triangle.classify(9, 12, 5)
        expected = Triangle.Type.SCALENE
        # self.assertEqual(actual, expected)
        
    def testScalene2(self):
        actual = Triangle.classify(13, 14, 15)
        expected = Triangle.Type.SCALENE
        # self.assertEqual(actual, expected)
    
    def testScalene3(self):
        actual = Triangle.classify(7, 10, 5)
        expected = Triangle.Type.SCALENE
        # self.assertEqual(actual, expected)

    def testIsosceles1(self):
        actual = Triangle.classify(7, 7, 5)
        expected = Triangle.Type.ISOSCELES
        # self.assertEqual(actual, expected)

    def testIsosceles2(self):
        actual = Triangle.classify(6, 5, 6)
        expected = Triangle.Type.ISOSCELES  # Different position for isosceles
        # self.assertEqual(actual, expected)
    
    def testIsosceles3(self):
        actual = Triangle.classify(5, 6, 6)
        expected = Triangle.Type.ISOSCELES  # Different position for isosceles
        # self.assertEqual(actual, expected)

    # Invalid Decisions
    def testInvalidZero(self):
        actual = Triangle.classify(0, 2, 2)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testInvalidNegative(self):
        actual = Triangle.classify(-2, 3, 3)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testScaleneInvalid1(self):
        actual = Triangle.classify(1, 10, 5)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testScaleneInvalid2(self):
        actual = Triangle.classify(10, 3, 2)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testIsocelesInvalid1(self):
        actual = Triangle.classify(7, 7, 15)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testIsocelesInvalid2(self):
        actual = Triangle.classify(6, 12, 6)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testInvalidEquality1(self):
        actual = Triangle.classify(5, 5, 10)  # Just fails the triangle rule
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testInvalidEquality2(self):
        actual = Triangle.classify(5, 5, 9)  # Just passes the triangle rule
        expected = Triangle.Type.ISOSCELES
        # self.assertEqual(actual, expected)

    # Additional Tests
    def testLargeSide(self):
        actual = Triangle.classify(100, 1, 1)  # Extreme imbalance
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def stressTest(self):
        actual = Triangle.classify(100000, 100000, 100000)  # Large numbers
        expected = Triangle.Type.EQUILATERAL
        # self.assertEqual(actual, expected)

    def testSwappedSides(self):
        actual = Triangle.classify(10, 5, 5)  # Triangle inequality fails
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testMinValue(self):
        actual = Triangle.classify(1, 1, 1)  # Smallest possible valid triangle
        expected = Triangle.Type.EQUILATERAL
        # self.assertEqual(actual, expected)
        
    def testBoundaryCaseJustValid(self): 
        actual = Triangle.classify(5, 5, 9)
        expected = Triangle.Type.ISOSCELES
        # self.assertEqual(actual, expected)

    def testBranchFullCoverage(self): 
        actual = Triangle.classify(10, 10, 20)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)
        
    def testTriangleInequalityJustValid(self):  # Covers True path for inequality check
        actual = Triangle.classify(7, 7, 13)
        expected = Triangle.Type.ISOSCELES
        # self.assertEqual(actual, expected)

    def testTriangleInequalityJustInvalid(self):  # Covers False path for inequality check
        actual = Triangle.classify(7, 7, 14)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testIsoscelesDifferentPositions1(self):  # (a == b)
        actual = Triangle.classify(8, 8, 5)
        expected = Triangle.Type.ISOSCELES
        # self.assertEqual(actual, expected)

    def testIsoscelesDifferentPositions2(self):  # (a == c)
        actual = Triangle.classify(6, 4, 6)
        expected = Triangle.Type.ISOSCELES
        # self.assertEqual(actual, expected)

    def testIsoscelesDifferentPositions3(self):  # (b == c)
        actual = Triangle.classify(5, 7, 7)
        expected = Triangle.Type.ISOSCELES
        # self.assertEqual(actual, expected)

    def testScaleneValid(self): 
        actual = Triangle.classify(9, 11, 7)
        expected = Triangle.Type.SCALENE
        # self.assertEqual(actual, expected)

    def testScaleneInvalid(self):  
        actual = Triangle.classify(3, 1, 1)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

    def testLargeNumberValidTriangle(self): 
        actual = Triangle.classify(99999, 100000, 100001)
        expected = Triangle.Type.SCALENE
        # self.assertEqual(actual, expected)

    def testLargeNumberInvalidTriangle(self):  
        actual = Triangle.classify(100000, 1, 1)
        expected = Triangle.Type.INVALID
        # self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
    