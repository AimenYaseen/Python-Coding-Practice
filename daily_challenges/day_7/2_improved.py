def improved_matching_string(input_string):
    odd = input_string[::2]
    even = input_string[1::2]

    if odd.islower() and even.isupper():
        return True
    return False


print(improved_matching_string('aNiMaL'))
print(improved_matching_string('animal'))
