def has_33(input_list):
    length = len(input_list) - 1
    for i in range(0, length):
        if input_list[i] == 3 and input_list[i + 1] == 3:
            return True
    return False


print(has_33([1, 2, 3]))  # False
print(has_33([1, 3, 3]))  # True
print(has_33([1, 3, 1, 3]))  # False
print(has_33([3, 1, 3]))  # False
print(has_33([3, 3, 1]))  # True
print(has_33([1, 2, 2, 3]))  # False
