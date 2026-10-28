import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    # --- Позитивные тесты (Positive / Valid inputs) ---

    def test_area_integer(self):
        """Проверка площади круга с целым радиусом"""
        res = area(5)
        self.assertAlmostEqual(res, math.pi * 25, places=5)

    def test_area_float(self):
        """Проверка площади круга с вещественным радиусом"""
        res = area(2.5)
        self.assertAlmostEqual(res, math.pi * 6.25, places=5)

    def test_area_zero(self):
        """Проверка площади круга с нулевым радиусом"""
        res = area(0)
        self.assertEqual(res, 0)

    def test_perimeter_integer(self):
        """Проверка длины окружности с целым радиусом"""
        res = perimeter(5)
        self.assertAlmostEqual(res, 2 * math.pi * 5, places=5)

    def test_perimeter_float(self):
        """Проверка длины окружности с вещественным радиусом"""
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 2 * math.pi * 2.5, places=5)

    def test_perimeter_zero(self):
        """Проверка длины окружности с нулевым радиусом"""
        res = perimeter(0)
        self.assertEqual(res, 0)

    # --- Негативные тесты (Negative / Boundary inputs) ---

    def test_area_negative(self):
        """Проверка площади круга с отрицательным радиусом: ожидается недопустимость вычисления"""
        res = area(-5)
        # Геометрически площадь не может быть положительной при отрицательном радиусе
        self.assertFalse(res > 0, "Функция area(-5) не должна возвращать положительную площадь для отрицательного радиуса")

    def test_perimeter_negative(self):
        """Проверка длины окружности с отрицательным радиусом: длина не может быть отрицательной"""
        res = perimeter(-5)
        self.assertGreaterEqual(res, 0, "Периметр окружности perimeter(-5) не может быть отрицательным")

    def test_area_type_error(self):
        """Проверка обработки некорректного типа данных (строка вместо числа)"""
        with self.assertRaises(TypeError):
            area("five")


if __name__ == "__main__":
    unittest.main()
