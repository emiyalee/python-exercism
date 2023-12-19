ROT = "abcdefghijklmnopqrstuvwxyz"
ROT += ROT


def rotate(text: str, key: int) -> str:
    string = []
    for c in text:
        if not c.isalpha():
            string.append(c)
            continue

        rot = ROT if c.islower() else ROT.upper()
        string.append(rot[rot.find(c) + key])

    return "".join(string)
