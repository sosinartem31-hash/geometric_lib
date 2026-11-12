def area(a, h):
    '''Принимает сторону a и высоту h треугольника, возвращает площадь.'''
    if a < 0 or h < 0:
        return 0
    return a * h / 2


def perimeter(a, b, c):
    '''Принимает стороны a, b, c треугольника, возвращает периметр.'''
    if a < 0 or b < 0 or c < 0:
        return 0
    if a + b <= c or a + c <= b or b + c <= a:
        return None
    return a + b + c
