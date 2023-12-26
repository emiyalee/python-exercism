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


def value(colors):
    seq = list(map(lambda x: expected.index(x), colors[:2]))
    return seq[0] * 10 + seq[1]


value(["brown", "black"])
