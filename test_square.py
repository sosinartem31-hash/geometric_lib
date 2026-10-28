import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    # --- Позитивные тесты (Positive / Valid inputs) ---

    def test_area_integer(self):
        """Проверка площади квадрата с целочисленной стороной"""
        res = area(4)
        self.assertEqual(res, 16)

    def test_area_float(self):
        """Проверка площади квадрата с вещественной стороной"""
        res = area(2.5)
        self.assertAlmostEqual(res, 6.25, places=5)

    def test_area_zero(self):
        """Проверка площади квадрата со стороной 0"""
        res = area(0)
        self.assertEqual(res, 0)

    def test_perimeter_integer(self):
        """Проверка периметра квадрата с целочисленной стороной"""
        res = perimeter(4)
        self.assertEqual(res, 16)

    def test_perimeter_float(self):
        """Проверка периметра квадрата с вещественной стороной"""
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 10.0, places=5)

    def test_perimeter_zero(self):
        """Проверка периметра квадрата со стороной 0"""
        res = perimeter(0)
        self.assertEqual(res, 0)

    # --- Негативные тесты (Negative / Boundary inputs) ---

    def test_area_negative(self):
        """Проверка площади квадрата с отрицательной стороной: геометрически сторона не может быть < 0"""
        res = area(-4)
        self.assertFalse(res > 0, "Функция area(-4) не должна возвращать положительную площадь для отрицательной стороны")

    def test_perimeter_negative(self):
        """Проверка периметра квадрата с отрицательной стороной: периметр не может быть < 0"""
        res = perimeter(-4)
        self.assertGreaterEqual(res, 0, "Периметр квадрата perimeter(-4) не может быть отрицательным")

    def test_area_type_error(self):
        """Проверка обработки некорректного типа данных (строка вместо числа)"""
        with self.assertRaises(TypeError):
            area("four")


if __name__ == "__main__":
    unittest.main()
