"""
Write a Python function to check whether a string is pangram or not.
Assume the string passed in does not have any punctuation.

Note:A pangram is a sentence containing every letter of the alphabet.
Example:
A quick brown fox jumps over the lazy dog.
"""


def is_pangram(input_str: str):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    for item in input_str:
        if item.lower() in alphabets:
            alphabets.remove(item.lower())

    if not alphabets:
        return "It is a Panagram"
    else:
        return "It is not Panagram"


string = "A quick brown fox jumps over the lazy dog."
print(is_pangram(string))
print(is_pangram("hashim"))
