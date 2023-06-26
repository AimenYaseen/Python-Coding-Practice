"""
In python, there is no parenthesis and curly brackets.
We use indentation to specify a piece of block instead of brackets or parenthesis.
So, If statements also don't need that
"""

n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

"""
But Parentheses needed for multi-line conditions.
Logical Operators
1. and = &&
2. or  = ||
"""
n, m = 1, 2
if ((n > 2 and
     n != m) or n == m):
    n += 1
