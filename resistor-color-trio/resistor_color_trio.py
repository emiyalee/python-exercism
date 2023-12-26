expected = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def label(colors: list[str]):
    colors = colors[0:3]

    v = 0
    for index, color in enumerate(colors[1::-1], 0):
        v += expected.index(color) * (10**index)

    if v == 0:
        return "0 ohms"

    zeros = 0
    while v % 10 == 0:
        zeros += 1
        v = v // 10

    zeros += expected.index(colors[-1])

    v = v * (10 ** (zeros % 3))
    unit = ""
    if zeros // 3 == 0:
        unit = "ohms"
    elif zeros // 3 == 1:
        unit = "kiloohms"
    elif zeros // 3 == 2:
        unit = "megaohms"
    else:
        unit = "gigaohms"

    return str(v) + " " + unit


print(label(["blue", "green", "yellow", "orange"]))
