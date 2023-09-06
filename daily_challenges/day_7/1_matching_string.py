"""
Define a function called myfunc that takes in a string,
and returns a matching string where every even letter is uppercase,
and every odd letter is lowercase.

Desired output:
myfunc('aNiMaL')-->True
"""


def matching_string(input_string):
    even = ''
    odd = ''

    for i in range(len(input_string)):
        if i % 2:
            even += (input_string[i])
        else:
            odd += (input_string[i])

    if odd.islower() and even.isupper():
        return True
    return False


print(matching_string('aNiMaL'))
print(matching_string('animal'))
