def test(strs):
    if len(strs) == 0:
        return ''
    index = 0
    result = ''
    while True:
        current = [s[index] for s in strs if len(s) > index]
        if len(current) != len(strs):
            return result
        if len(list(set(current))) != 1:
            return result
        result += current[0]
        index += 1

    return result

print(test(["abca","abc"]))
print(test(["c","c"]))
print(test([""]))