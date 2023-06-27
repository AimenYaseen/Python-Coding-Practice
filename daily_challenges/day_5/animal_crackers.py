"""
Write a function takes a two-word string and returns True if both words begin with same letter
"""


def animal_crackers(input_string):
    input_list = input_string.lower().split(' ')
    if input_list[0][0] == input_list[1][0]:
        return True
    return False


print(animal_crackers('Crazy Chocolate'))
print(animal_crackers('Lazy Dog'))
