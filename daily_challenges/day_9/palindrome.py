"""
Write a Python function that checks whether a word or phrase is palindrome or not.
Example of Palindrome:
Hannah
Anna
"""


def palindrome(input_string):
    # input_string[::-1] => reverse the string
    return input_string.lower() == input_string[::-1].lower()


print(palindrome("Hannah"))
print(palindrome("Anna"))
