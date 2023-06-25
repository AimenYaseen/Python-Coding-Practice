"""
Problem Statement: If the two numbers are even return the smaller number otherwise greater
"""

# short circuit technique in python
lesser_of_two_evens = lambda x, y: (x % 2 or y % 2) and max(x, y) or min(x, y)

print(lesser_of_two_evens(3, 4))
print(lesser_of_two_evens(2, 2))
print(lesser_of_two_evens(10, 2))
