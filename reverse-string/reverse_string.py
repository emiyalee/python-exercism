def reverse(text):
    s = []
    for c in text:
        s.insert(0, c)

    return "".join(s)
