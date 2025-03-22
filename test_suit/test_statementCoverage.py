import unittest
from isTriangle import Triangle

class TestStatementCoverage(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(Triangle.classify(6, 6, 6), Triangle.Type.EQUILATERAL)

    def test_scalene(self):
        self.assertEqual(Triangle.classify(7, 10, 5), Triangle.Type.SCALENE)

    def test_isosceles(self):
        self.assertEqual(Triangle.classify(6, 6, 4), Triangle.Type.ISOSCELES)

    def test_invalid_zero(self):
        self.assertEqual(Triangle.classify(0, 5, 5), Triangle.Type.INVALID)

    def test_invalid_negative(self):
        self.assertEqual(Triangle.classify(-3, 4, 5), Triangle.Type.INVALID)

    def test_invalid_triangle_inequality_1(self):
        self.assertEqual(Triangle.classify(1, 2, 3), Triangle.Type.INVALID)

    def test_invalid_triangle_inequality_2(self):
        self.assertEqual(Triangle.classify(5, 1, 1), Triangle.Type.INVALID)  # Edge case  

    def test_large_numbers(self):
        self.assertEqual(Triangle.classify(100000, 100000, 100000), Triangle.Type.EQUILATERAL)  # Stress test

if __name__ == '__main__':
    unittest.main()