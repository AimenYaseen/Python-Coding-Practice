"""
********DAY 10********

Python coding question:
Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24
"""


def multiply_numbers(input_list: list()):
    result = 1

    for item in input_list:
        result *= item

    return result


print(multiply_numbers([1, 2, 3, -4]))
