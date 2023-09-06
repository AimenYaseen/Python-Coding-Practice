"""
********DAY 12********
Python coding question:

Write a code to check whether a year is leap year or not.
Note:A year that is evenly divisible by 100 is a leap year only if it is also evenly divisible by 400.

A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year
only if it is perfectly divisible by 400.


A year is a leap year if the following conditions are satisfied:

The year is multiple of 400.
The year is multiple of 4 and not multiple of 100.

Desired Output:
is_leap(1996)-->Leap year
is_leap(2100)-->not a Leap year
is_leap(2000)—>Leap year
"""


def leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


print(leap_year(1996))
print(leap_year(2100))
print(leap_year(2000))
