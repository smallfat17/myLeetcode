'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
'''


def divide(dividend, divisor):
    if divisor == 0:
        return -1
    absdividend = abs(dividend)
    absdivisor = abs(divisor)
    result = 0
    current_time = 1
    current_divisor = absdivisor
    while absdividend >= absdivisor:
        # print(absdividend,current_divisor)
        # print(current_time)
        if current_divisor > absdividend:
            current_divisor = absdivisor
            current_time = 1
        absdividend -= current_divisor
        result += current_time
        current_divisor = current_divisor + current_divisor
        current_time += current_time

    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        result = 0 - result
    if result > 2 ** 31 - 1 or result < -(2 ** 31):
        return 2 ** 31 - 1
    return result

print(divide(-2147483648,-1))