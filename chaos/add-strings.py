#coding:utf-8
'''
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
'''

def addStrings(num1,num2):
    index = 0
    num1,num2 = num1[::-1],num2[::-1]
    r = ''
    # flag = False
    front = 0
    while index < len(num1) and index < len(num2):
        print(front)
        current = int(num1[index]) + int(num2[index])
        print(current)
        if front:
            current += front
            # flag = False
        if current >= 10:
            front = int(current / 10)
            # flag = True
            current %= 10
        r += str(current)
        index += 1

    # print(front)
    if index < len(num1):
        while index < len(num1):
            current = int(num1[index])
            if front:
                print(type(current),type(front))
                current += front
            if current >= 10:
                front = int(current / 10)
                # flag = True
                current %= 10

            r += str(current)
            index += 1

    elif index < len(num2):
        while index < len(num2):
            current = int(num2[index])
            if front:
                front = int(current / 10)
            if current >= 10:
                front /= int(10)
                # flag = True
                current %= 10
            r += str(current)
            index += 1
    elif front:
        r += '1'

    return r[::-1]

print(addStrings("1","999"))
