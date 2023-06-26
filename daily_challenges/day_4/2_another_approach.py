import string


def is_panagram(input_string):
    alphabets = string.ascii_lowercase

    for char in alphabets:
        if char not in input_string.lower():
            return "It is not Pangram"
    return "It is Pangram"


test = "A quick brown fox jumps over the lazy dog."
print(is_panagram(test))
print(is_panagram("hashim"))


def is_pangram(_string):
    _string = _string.lower()
    # chr() convert digits from 97-123 to its ascii lower case character
    charset = [chr(i) for i in range(97, 123)]
    for char in charset:
        if char not in _string:
            return False
    return True

# Time Complexity - O(N)
# Space Complexity - O(1)
