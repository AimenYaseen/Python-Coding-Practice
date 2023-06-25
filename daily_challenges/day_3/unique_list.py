"""
Write a Python function that takes a list
and returns a new list with unique elements
of the first list.
"""


def unique_list(input_list):
    return list(set(input_list))


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))
