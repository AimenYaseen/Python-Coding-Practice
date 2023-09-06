"""
Python have two loops, while and for loop.

While loop is used when you don't know about the number of iterations.
Example, you have to take input from user repeatedly until it enters correct input.

For loop is used when you know about the number of iterations.
Example, print a number 10 times.

"""

n = 5
while n < 5:
    print(n)
    n += 1

"""
We use range function for iteration in for loop.
Some facts about range function:
1. By default, it starts with 0.
2. range(stop_value) equals to i < stop_value. It means last digit is always exclusive.
3. You can also specify the starting value like this => range(start, stop).
4. By default, it increments by +1.
5. You can also specify the incrementing value like this => range(start, stop, increment).
"""

# Looping from i = 0 to i = 4
for i in range(5):
    print(i)

# Looping from i = 2 to i = 5
for i in range(2, 6):
    print(i)

# Looping from i = 5 to i = 2 with -1 increment
for i in range(5, 1, -1):
    print(i)
