def area(a, b):
    '''Принимает длины сторон a и b прямоугольника, возвращает площадь.'''
    if a < 0 or b < 0:
        return 0
    return a * b


def perimeter(a, b):
    '''Принимает длины сторон a и b прямоугольника, возвращает периметр.'''
    if a < 0 or b < 0:
        return 0
    return 2 * (a + b)
