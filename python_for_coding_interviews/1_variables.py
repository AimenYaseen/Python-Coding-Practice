"""
In python , variables are dynamically typed.
It means their data type is determined at runtime.
No need to specify their datatype like we do in c++ e.g. int x;
"""

n = 0
print('n =', n)
# n = 0

n = "abc"
print('n =', n)
# n = abc

# Multiple assignments
n, m = 0, "abc"
n, m, z = 0.125, "abc", False

# Increment
n = n + 1  # good
n += 1  # good
# n++       # bad; there is no such operator in python

# None is null (absence of value)
n = 4
n = None
print("n =", n)
# n = None
