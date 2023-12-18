def convert(number):
    v = ""
    if number % 3 == 0:
        v += "Pling"

    if number % 5 == 0:
        v += "Plang"

    if number % 7 == 0:
        v += "Plong"

    if len(v) == 0:
        return "{0}".format(number)

    return v
