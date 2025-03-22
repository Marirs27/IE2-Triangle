import unittest
from isTriangle import Triangle

class TestDecisionCoverage(unittest.TestCase):

    # Valid Decisions
    def testEquilateral(self):
        self.assertEqual(Triangle.classify(8, 8, 8), Triangle.Type.EQUILATERAL)

    def testScalene1(self):
        self.assertEqual(Triangle.classify(9, 12, 5), Triangle.Type.SCALENE)
        
    def testScalene2(self):
        self.assertEqual(Triangle.classify(13,14,15), Triangle.Type.SCALENE)
    
    def testScalene3(self):
        self.assertEqual(Triangle.classify(7,10,5), Triangle.Type.SCALENE)

    def testIsosceles1(self):
        self.assertEqual(Triangle.classify(7, 7, 5), Triangle.Type.ISOSCELES)

    def testIsosceles2(self):
        self.assertEqual(Triangle.classify(6, 5, 6), Triangle.Type.ISOSCELES)  # Different position for isosceles
    
    def testIsosceles3(self):
        self.assertEqual(Triangle.classify(5, 6, 6), Triangle.Type.ISOSCELES)  # Different position for isosceles

    # Invalid Decisions
    def testInvalidZero(self):
        self.assertEqual(Triangle.classify(0, 2, 2), Triangle.Type.INVALID)

    def testInvalidNegative(self):
        self.assertEqual(Triangle.classify(-2, 3, 3), Triangle.Type.INVALID)

    def testScaleneInvalid1(self):
        self.assertEqual(Triangle.classify(1, 10, 5), Triangle.Type.INVALID)

    def testScaleneInvalid2(self):
        self.assertEqual(Triangle.classify(10, 3, 2), Triangle.Type.INVALID)

    def testIsocelesInvalid1(self):
        self.assertEqual(Triangle.classify(7, 7, 15), Triangle.Type.INVALID)

    def testIsocelesInvalid2(self):
        self.assertEqual(Triangle.classify(6, 12, 6), Triangle.Type.INVALID)

    def testInvalidEquality1(self):
        self.assertEqual(Triangle.classify(5, 5, 10), Triangle.Type.INVALID)  # Just fails the triangle rule

    def testInvalidEquality2(self):
        self.assertEqual(Triangle.classify(5, 5, 9), Triangle.Type.ISOSCELES)  # Just passes the triangle rule


    # Additional Tests
    def testLargeSide(self):
        self.assertEqual(Triangle.classify(100, 1, 1), Triangle.Type.INVALID)  # Extreme imbalance

    def stressTest(self):
        self.assertEqual(Triangle.classify(100000, 100000, 100000), Triangle.Type.EQUILATERAL)  # Large numbers

    def testSwappedSides(self):
        self.assertEqual(Triangle.classify(10, 5, 5), Triangle.Type.INVALID)  # Triangle inequality fails

    def testMinValue(self):
        self.assertEqual(Triangle.classify(1, 1, 1), Triangle.Type.EQUILATERAL)  # Smallest possible valid triangle
        
    def testBoundaryCaseJustValid(self): 
        self.assertEqual(Triangle.classify(5, 5, 9), Triangle.Type.ISOSCELES) 

    def testBranchFullCoverage(self): 
        self.assertEqual(Triangle.classify(10, 10, 20), Triangle.Type.INVALID)  
        
    def testTriangleInequalityJustValid(self):  # Covers True path for inequality check
        self.assertEqual(Triangle.classify(7, 7, 13), Triangle.Type.ISOSCELES)  

    def testTriangleInequalityJustInvalid(self):  # Covers False path for inequality check
        self.assertEqual(Triangle.classify(7, 7, 14), Triangle.Type.INVALID)  

    def testIsoscelesDifferentPositions1(self):  # (a == b)
        self.assertEqual(Triangle.classify(8, 8, 5), Triangle.Type.ISOSCELES)  

    def testIsoscelesDifferentPositions2(self):  # (a == c)
        self.assertEqual(Triangle.classify(6, 4, 6), Triangle.Type.ISOSCELES)  

    def testIsoscelesDifferentPositions3(self):  # (b == c)
        self.assertEqual(Triangle.classify(5, 7, 7), Triangle.Type.ISOSCELES)  

    def testScaleneValid(self): 
        self.assertEqual(Triangle.classify(9, 11, 7), Triangle.Type.SCALENE)  

    def testScaleneInvalid(self):  
        self.assertEqual(Triangle.classify(3, 1, 1), Triangle.Type.INVALID)  

    def testLargeNumberValidTriangle(self): 
        self.assertEqual(Triangle.classify(99999, 100000, 100001), Triangle.Type.SCALENE)  

    def testLargeNumberInvalidTriangle(self):  
        self.assertEqual(Triangle.classify(100000, 1, 1), Triangle.Type.INVALID)  



if __name__ == '__main__':
    unittest.main()
