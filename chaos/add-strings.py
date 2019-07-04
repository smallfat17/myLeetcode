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
    if not num1:
        return
    m = len(num1) - 1
    n = len(num2) - 1
    result = ""
    step = 0
    while m >= 0 or n >= 0 or step:
        a = 0
        b = 0
        if m >= 0:
            a = int(num1[m])
        if n >= 0:
            b = int(num2[n])
        current = a + b + step
        step = current // 10
        offset = current % 10
        result += str(offset)
        m -= 1
        n -= 1

    return result[::-1]


print(addStrings("23","1"))
