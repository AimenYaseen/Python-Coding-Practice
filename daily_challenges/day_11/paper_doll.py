"""
Python coding question:

Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

This one's interesting :D
"""


def paper_doll(input_string):
    result = ""

    for item in input_string:
        result += (item * 3)

    return result


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

# 2nd Approach
_result = [i * 3 for i in 'Hello']
print("".join(_result))
