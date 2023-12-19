def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    total = 0
    n = 1
    while n < number - 1:
        if not number % n:
            total += n
        n += 1

    if total < number:
        return "deficient"

    if total == number:
        return "perfect"

    return "abundant"
