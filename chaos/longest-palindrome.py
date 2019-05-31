#coding: utf-8
'''
定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
'''
def longestPalindrome(s):
    if len(s) == 0:
        return 0
    d = {}
    for i in s:
        d[i] = d.get(i,0)+1
    print(d)
    l = 0
    flag = True
    for k in d:
        if d[k] % 2 == 0:
            l += d[k]
        else:
            l += d[k] -1
            if flag:
                l += 1
                flag = False
    return l
print(longestPalindrome('a'))
