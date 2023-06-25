"""
Problem Statement: If the two numbers are even return the smaller number otherwise greater
"""


def lesser_of_two_evens(num1, num2):
    if num1 > num2:
        greater = num1
        lesser = num2
    else:
        greater = num2
        lesser = num1

    if num1 % 2 == 0 and num2 % 2 == 0:
        return lesser
        # return num1 if num1 < num2 else num2
    else:
        return greater


print(lesser_of_two_evens(3, 4))
print(lesser_of_two_evens(2, 2))
print(lesser_of_two_evens(10, 2))
