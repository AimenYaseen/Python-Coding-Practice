"""
Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False
"""


def spy_game(input_list):
    spy_list = []

    for item in input_list:
        if len(spy_list) == 3:
            break
        if item == 0 and spy_list.count(0) < 2:
            spy_list.append(item)
        elif item == 7 and spy_list.count(7) < 1:
            spy_list.append(item)

    if spy_list == [0, 0, 7]:
        return True
    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 2, 4, 0, 0, 0, 5, 7, 8, 0]))


# It only checks for consecutive 007

def spy_game(spy_list):
    spy_list = [str(i) for i in spy_list]
    return True if '007' in (''.join(spy_list)) else False
