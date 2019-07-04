'''
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
'''


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if len(needle) == 0:
        return 0
    if len(haystack) == 0:
        return -1
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            if haystack[i: i+len(needle)] == needle:
                return i
    return -1

# print(strStr('abdsaidnsioaddd','nsi'))
# a = 3
# b = 2
# a,b = b,a
# print(a,b)
from collections.abc import Iterator

class Nums:
    def __init__(self, nums):
        self.nums = nums
        self.index = 0

    def __iter__(self):
        return self
        # return MyIterator(self.nums)

    def __next__(self):
        if self.index < len(self.nums):
            data = self.nums[self.index]
            self.index += 1
            return data
        else:
            raise StopIteration




# class MyIterator(Iterator):
#     def __init__(self, nums):
#         self.nums = nums
#         self.index = 0
#
#     def __getitem__(self, item):
#         return self.nums[item]
#
#     def __next__(self):
#         try:
#             data = self.nums[self.index]
#         except:
#             raise StopIteration
#         self.index += 1
#         return data

nums = Nums([1,2,3])
# for num in nums:
#     print(num)

# for i in nums:
#     print(i)
try:
    while next(nums):
        print('ok')
except StopIteration:
    pass