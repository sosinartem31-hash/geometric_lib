import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    # --- Позитивные тесты (Positive / Valid inputs) ---

    def test_area_integer(self):
        """Проверка вычисления площади треугольника с целыми стороной и высотой"""
        res = area(6, 4)
        self.assertAlmostEqual(res, 12.0, places=5)

    def test_area_float(self):
        """Проверка площади треугольника с вещественными числами"""
        res = area(5.5, 2.0)
        self.assertAlmostEqual(res, 5.5, places=5)

    def test_area_zero(self):
        """Проверка площади треугольника с нулевым основанием"""
        res = area(0, 4)
        self.assertEqual(res, 0.0)

    def test_perimeter_integer(self):
        """Проверка периметра треугольника со сторонами 3, 4, 5 (египетский треугольник)"""
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_float(self):
        """Проверка периметра треугольника с вещественными сторонами"""
        res = perimeter(2.5, 3.5, 4.0)
        self.assertAlmostEqual(res, 10.0, places=5)

    def test_perimeter_equilateral(self):
        """Проверка периметра равностороннего треугольника со стороной 7"""
        res = perimeter(7, 7, 7)
        self.assertEqual(res, 21)

    # --- Негативные тесты (Negative / Boundary inputs) ---

    def test_area_negative(self):
        """Проверка площади треугольника с отрицательным основанием: ожидается недопустимость вычисления"""
        res = area(-6, 4)
        self.assertFalse(res < 0, "Площадь треугольника area(-6, 4) не может быть отрицательной величиной")

    def test_perimeter_negative(self):
        """Проверка периметра треугольника с отрицательными сторонами: периметр не может быть отрицательным"""
        res = perimeter(-3, -4, -5)
        self.assertGreaterEqual(res, 0, "Периметр треугольника perimeter(-3, -4, -5) не может быть отрицательным")

    def test_triangle_inequality_invalid(self):
        """Проверка расчета периметра несуществующего треугольника (стороны 1, 2, 10 нарушают неравенство треугольника)"""
        a, b, c = 1, 2, 10
        # В евклидовой геометрии сумма двух сторон треугольника всегда строго больше третьей
        if not (a + b > c and a + c > b and b + c > a):
            res = perimeter(a, b, c)
            self.assertIsNone(res, "Для сторон 1, 2, 10 треугольник не существует, периметр не должен вычисляться")

    def test_area_type_error(self):
        """Проверка обработки некорректного типа данных (строки вместо чисел)"""
        with self.assertRaises(TypeError):
            area("six", "four")


if __name__ == "__main__":
    unittest.main()
