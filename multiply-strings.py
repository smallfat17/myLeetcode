'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
'''
from functools import reduce
import time

def count_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result =  func(*args, **kwargs)
        print(time.time() - start)
        return result
    return wrapper

class Solution(object):
    @count_time
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return reduce(self.add_strings,[self.multiply_one_bit(num1, num2[i])+("0"*(len(num2) - 1 - i)) for i in range(len(num2))])

    def multiply_one_bit(self,num1, num):
        m = len(num1) - 1
        step = 0
        result = ""
        while m >= 0 or step:
            a = 0
            if m>=0:
                a = int(num1[m])
            current = a * int(num) + step
            step = current // 10
            offset = current % 10
            result += str(offset)
            m -= 1
        return result[::-1]

    def add_strings(self, num1, num2):
        m, n = len(num1)-1, len(num2)-1
        step = 0
        result = ""
        while m>=0 or n>=0 or step:
            a, b = 0, 0
            if m>=0:
                a = int(num1[m])
            if n>=0:
                b = int(num2[n])
            current = a + b + step
            step = current // 10
            offset = current % 10
            result += str(offset)
            m -= 1
            n -= 1
        return result[::-1]


if __name__ == '__main__':
    result = Solution().multiply("55115457894121545415948942123459789745615456456415645648941521564564649874521231231654897894561231548978945132156489795123894123123", "20012456744123156489789456123123456489789748945615231564890498456012301506408978948121412345678745212345648948475641231564")
    print(result)

