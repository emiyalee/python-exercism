def is_pangram(sentence):
    sentence = sentence.lower()
    s = set()
    for c in sentence:
        if c.isalpha():
            s.add(c)

    return len(s) == 26
