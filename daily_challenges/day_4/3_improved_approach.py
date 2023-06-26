import string


def is_panagram(str1):
    # Create a set of the alphabet of the string passed
    alphabet = string.ascii_lowercase
    alpha_set = set(alphabet)

    # Remove spaces from str1
    str1 = str1.replace(" ", '')

    # Lowercase all strings and assigned back to string
    # Recall we assume no punctuation
    str1 = str1.lower()

    # Grab all unique letters in the string as a set
    str1 = set(str1)
    print(str1)

    # Now check that the alphabet set is same as string set
    return str1 == alpha_set


test = "A quick brown fox jumps over the lazy dog"
print(is_panagram(test))
print(is_panagram("hashim"))
