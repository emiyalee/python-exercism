def is_isogram(string: str) -> bool:
    string = string.replace(" ", "").replace("-", "").lower()
    return len(set(string.lower())) == len(string)
