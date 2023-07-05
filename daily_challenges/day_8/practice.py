import re


def upper_lower_count(string):
    lower_count, upper_count = 0, 0
    x = re.findall("[a-zA-z]", string)
    for i in range(0, len(x)):
        if x[i] == x[i].lower():
            lower_count = lower_count + 1
        else:
            upper_count = upper_count + 1
    return f"Count of upper case chars is {upper_count}, and count of lower case chars is {lower_count}"


# testing the fn.
str_test_1 = 'Hello Mr. Rogers, how are you this fine Tuesday?'
upper_lower_count(str_test_1)
# output
'Count of upper case chars is 4, and count of lower case chars is 33'
