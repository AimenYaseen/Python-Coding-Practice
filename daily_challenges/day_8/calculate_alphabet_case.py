"""
Write a Python function that accepts a string and calculates the number of upper case letters
and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output :
No. of Upper case characters : 4
No. of Lower case Characters : 33
"""


def calculate_alpha_case(input_string):
    upper = 0
    lower = 0

    for item in input_string:
        if item.isupper():
            upper += 1
        elif item.islower():
            lower += 1

    return f"No. of Upper case characters : {upper}\nNo. of Lower case Characters : {lower}"


print(calculate_alpha_case('Hello Mr. Rogers, how are you this fine Tuesday?'))
