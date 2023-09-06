from functools import reduce

input_list = [1, 2, 3, -4]

result = reduce((lambda x, y: x*y), input_list)
print(result)

"""
walrus operator
enumerate:  list of lists

-----------------------------------------------------------------
reduce
reduce ==> take the numbers in the list,
combines the first number with the second, perform operation and
then combines the result with the third, and so on

you must imported ==> from functools import reduce

Examples :-

my_list = [1, 2, 8, 50, 90]

result = reduce(lambda num1, num2: num1 + num2, my_list)

my_list = [ 1, 2, 8, 50, 90 ]  ==> 1 + 2 = 3 / 3 + 8 = 11 / 11 + 50 = 61 / 61 + 90 = 151
"""
