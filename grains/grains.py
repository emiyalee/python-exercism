def square(number: int) -> int:
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    return 1 << (number - 1)


def total():
    return sum([square(x) for x in range(1, 65)])
