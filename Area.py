import math


class GeometryCalculator:
    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(side1, side2, side3):
        # Полупериметр треугольника
        s = (side1 + side2 + side3) / 2
        # Площадь треугольника по формуле Герона
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area

    @staticmethod
    def is_right_triangle(side1, side2, side3):
        sides = [side1, side2, side3]
        sides.sort()
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)


c = GeometryCalculator()
print(c.circle_area(2))
