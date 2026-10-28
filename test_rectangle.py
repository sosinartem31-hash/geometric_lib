import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    # --- Тесты из примера методических указаний ---

    def test_zero_mul(self):
        """Проверка площади прямоугольника при нулевой стороне (из методички)"""
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        """Проверка площади квадрата через прямоугольник 10x10 (из методички)"""
        res = area(10, 10)
        self.assertEqual(res, 100)

    # --- Позитивные тесты (Positive / Valid inputs) ---

    def test_area_integer(self):
        """Проверка площади прямоугольника с целыми сторонами"""
        res = area(10, 20)
        self.assertEqual(res, 200)

    def test_area_float(self):
        """Проверка площади прямоугольника с вещественными сторонами"""
        res = area(2.5, 4.0)
        self.assertAlmostEqual(res, 10.0, places=5)

    def test_perimeter_integer(self):
        """Проверка периметра прямоугольника с целыми сторонами"""
        res = perimeter(10, 20)
        self.assertEqual(res, 60)

    def test_perimeter_float(self):
        """Проверка периметра прямоугольника с вещественными сторонами"""
        res = perimeter(2.5, 4.0)
        self.assertAlmostEqual(res, 13.0, places=5)

    def test_perimeter_zero(self):
        """Проверка периметра вырожденного прямоугольника со стороной 0"""
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    # --- Негативные тесты (Negative / Boundary inputs) ---

    def test_area_negative(self):
        """Проверка площади прямоугольника с отрицательной стороной"""
        res = area(-10, 20)
        self.assertFalse(res < 0, "Площадь прямоугольника area(-10, 20) не может быть отрицательной величиной")

    def test_perimeter_negative(self):
        """Проверка периметра прямоугольника с отрицательными сторонами"""
        res = perimeter(-10, -20)
        self.assertGreaterEqual(res, 0, "Периметр прямоугольника perimeter(-10, -20) не может быть отрицательным")

    def test_area_string_type(self):
        """Проверка передачи нечисловых аргументов (строки вместо чисел)"""
        with self.assertRaises(TypeError):
            area("ten", "twenty")


if __name__ == "__main__":
    unittest.main()
