import re


def matching_str():
    word = 'aNiMaL'
    func = lambda x: (x[0] % 2 == 0 and x[1].islower()) or (x[0] % 2 != 0 and x[1].isupper())
    return len(word) == len(list(filter(func, list(enumerate(word)))))


# using regex
def myfunc(s):
    return False if (len(s) == 0) else bool(re.fullmatch(r'([a-z][A-Z])*[a-z]?', s))
