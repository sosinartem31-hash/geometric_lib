def area(a):
    '''Принимает сторону a квадрата, возвращает площадь.'''
    if a < 0:
        return 0
    return a * a


def perimeter(a):
    '''Принимает сторону a квадрата, возвращает периметр.'''
    if a < 0:
        return 0
    return 4 * a
