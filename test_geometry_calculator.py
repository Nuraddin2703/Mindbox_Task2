import unittest
from Area import GeometryCalculator


class TestGeometryCalculator(unittest.TestCase):
    def test_circle_area(self):
        # Проверка вычисления площади круга
        self.assertAlmostEqual(GeometryCalculator.circle_area(5), 78.54, places=2)
        self.assertAlmostEqual(GeometryCalculator.circle_area(0), 0)

    def test_triangle_area(self):
        # Проверка вычисления площади треугольника
        self.assertAlmostEqual(GeometryCalculator.triangle_area(3, 4, 5), 6)
        self.assertAlmostEqual(GeometryCalculator.triangle_area(6, 8, 10), 24)
        self.assertAlmostEqual(GeometryCalculator.triangle_area(5, 12, 13), 30)

    def test_is_right_triangle(self):
        # Проверка определения прямоугольного треугольника
        self.assertTrue(GeometryCalculator.is_right_triangle(3, 4, 5))
        self.assertFalse(GeometryCalculator.is_right_triangle(3, 3, 3))
        self.assertFalse(GeometryCalculator.is_right_triangle(5, 6, 7))

