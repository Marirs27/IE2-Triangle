import unittest
from isTriangle import Triangle

class TestStatementCoverage(unittest.TestCase):

    # Valid Triangles
    def testEquilateral(self):
        self.assertEqual(Triangle.classify(16, 16, 16), Triangle.Type.EQUILATERAL)

    def testScalene(self):
        self.assertEqual(Triangle.classify(7, 10, 5), Triangle.Type.SCALENE)

    def testIsosceles1(self):
        self.assertEqual(Triangle.classify(26, 26, 24), Triangle.Type.ISOSCELES)

    def testIsosceles2(self):
        self.assertEqual(Triangle.classify(15, 13, 15), Triangle.Type.ISOSCELES) 

    # Invalid Triangles
    def testInvalidZero(self):
        self.assertEqual(Triangle.classify(0, 51, 51), Triangle.Type.INVALID)

    def testInvalidNegative(self):
        self.assertEqual(Triangle.classify(-10, 4, 5), Triangle.Type.INVALID)

    def testInvalidInequality1(self):
        self.assertEqual(Triangle.classify(1, 2, 3), Triangle.Type.INVALID)

    def testInvalidInequality2(self):
        self.assertEqual(Triangle.classify(50, 10, 10), Triangle.Type.INVALID)

    def testInvalidInequality3(self):
        self.assertEqual(Triangle.classify(101, 100, 1), Triangle.Type.INVALID) 

    def testInvalidInequality4(self):
        self.assertEqual(Triangle.classify(6, 10, 3), Triangle.Type.INVALID) 

    # Edge and Boundary Cases
    def testBoundaryCase(self):
        self.assertEqual(Triangle.classify(10, 10, 20), Triangle.Type.INVALID) 

    def testStressTestScalene(self):
        self.assertEqual(Triangle.classify(999999, 1000000, 1000001), Triangle.Type.SCALENE) 

    def testStressTestEquilateral(self):
        self.assertEqual(Triangle.classify(1010001, 1010001, 1010001), Triangle.Type.EQUILATERAL) 
        
    def testStressTestIsosceles(self):
        self.assertEqual(Triangle.classify(1010000, 1010001, 1010001), Triangle.Type.ISOSCELES) 
        
    # Error Cases
    def testStringInput(self):  # Expecting TypeError or INVALID handling
        with self.assertRaises(TypeError):
            Triangle.classify("a", "b", "c")

    def testMixedInput(self):  # Integer + String Mix
        with self.assertRaises(TypeError):
            Triangle.classify(5, "b", 7)

    def testListInput(self):  # Passing a list instead of an integer
        with self.assertRaises(TypeError):
            Triangle.classify([3, 4, 5], 4, 5)

    def testNoneInput(self):  # Passing None as input
        with self.assertRaises(TypeError):
            Triangle.classify(None, 4, 5)

if __name__ == '__main__':
    unittest.main()