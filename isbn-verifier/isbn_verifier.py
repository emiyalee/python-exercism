def is_valid(isbn: str) -> bool:
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False

    if not isbn[:-1].isdigit() or (not isbn[-1].isdigit() and isbn[-1] != "X"):
        return False

    total = 0

    for index, ch in enumerate(isbn, 0):
        num = 10 if ch == "X" else int(ch)
        total += num * (10 - index)

    return not total % 11
