def is_armstrong_number(number):
    a = len(str(number))
    s = 0
    for c in str(number):
        s += int(c) ** a

    return s == number

