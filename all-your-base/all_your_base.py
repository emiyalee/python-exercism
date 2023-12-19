def rebase(input_base: int, digits: list[int], output_base: int):
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    for digit in digits:
        if not 0 <= digit < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    number = 0

    for index, digit in enumerate(digits, 1):
        number += digit * (input_base ** (len(digits) - index))

    if number == 0:
        return [0]

    new_digits: list[int] = []

    while number != 0:
        new_digits.insert(0, number % output_base)
        number = number // output_base

    return new_digits


rebase(10, [4, 2], 2)
