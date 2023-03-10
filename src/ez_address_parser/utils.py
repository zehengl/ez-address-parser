from re import split
from string import punctuation

puncts = punctuation.replace("#", "")


def tokenize(s):
    s = s.replace("#", " # ")
    return [token for token in split(fr"[{puncts}\s]+", s) if token]
