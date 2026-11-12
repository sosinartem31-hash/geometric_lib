import math


def area(r):
    '''Принимает радиус r круга, возвращает площадь круга.'''
    if r < 0:
        return 0
    return math.pi * r * r


def perimeter(r):
    '''Принимает радиус r круга, возвращает длину окружности.'''
    if r < 0:
        return 0
    return 2 * math.pi * r
