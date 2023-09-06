import math

# Division is decimal by default
print('5 / 2 = ', 5 / 2)
# output => 2.5

# Double slash rounds down to integer
print('5 // 2 = ', 5 // 2)
# output => 2

# CAREFUL: most languages round towards 0 by default
# python rounds towards minimum value
# So negative numbers will round down
print('-3 // 2 = ', -3 // 2)
# output => -2 but it should be -1

# A workaround for rounding towards zero
# is to use decimal division and then convert to int.
print('-3 // 2 = ', int(-3 / 2))
# output => -1

# Modding is similar to most languages
print('10 % 3 = ', 10 % 3)
# output => 1

# Except for negative values
print('-10 % 3 = ', -10 % 3)

# To be consistent with other languages modulo use math fmod

print(math.fmod(-10, 3))

# More math helpers
print(math.floor(3 / 2))  # rounds down
print(math.ceil(3 / 2))  # rounds up
print(math.sqrt(2))
print(math.pow(2, 3))

# Max / Min Int
float("inf")
float("-inf")

# Python numbers are infinite so they never overflow
print(math.pow(2, 200))

# But still less than infinity
print(math.pow(2, 200) < float("inf"))
# output => True
