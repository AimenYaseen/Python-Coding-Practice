"""
Problem Statement: If the two numbers are even return the smaller number otherwise greater
"""


def lesser_of_two_evens(num1, num2):
    return min(num1, num2) if (num1 % 2 == 0 and num2 % 2 == 0) else max(num1, num2)


print(lesser_of_two_evens(3, 4))
print(lesser_of_two_evens(2, 2))
print(lesser_of_two_evens(10, 2))


def lesser_args(*args):
    return max(args) if any(arg % 2 != 0 for arg in args) else min(args)
