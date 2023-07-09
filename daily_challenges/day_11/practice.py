def convert(s):
    result = [None] * (len(s) * 3)
    i, j = 0, len(s) - 1
    while i <= j:
        for m in range(3):
            result[3 * i + m] = s[i]
            result[-(3 * i + m + 1)] = s[j]
        i += 1
        j -= 1
    return ''.join(result)


print(convert('hello'))
print(convert('mississippi'))

# Time complexity=O(3n/2)
