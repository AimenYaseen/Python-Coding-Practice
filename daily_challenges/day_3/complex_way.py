# Its time complexity is O(n)

def unique_list(input_list):
    unique = []
    for item in input_list:
        if item not in unique:
            unique.append(item)
    return unique


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))
