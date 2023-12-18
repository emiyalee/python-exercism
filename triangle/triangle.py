def is_triangle(sides: list[float]):
    if len(sides) != 3:
        return False

    a, b, c = sides
    if a <= 0 or b < 0 or c < 0:
        return False

    if a + b < c or a + c < b or b + c < a:
        return False

    return True


def equilateral(sides):
    if not is_triangle(sides):
        return False

    a, b, c = sides
    return a == b == c


def isosceles(sides):
    if not is_triangle(sides):
        return False

    a, b, c = sides

    return a == b or b == c or a == c


def scalene(sides):
    if not is_triangle(sides):
        return False

    a, b, c = sides

    return a != b and b != c and a != c
