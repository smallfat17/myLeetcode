#coding:utf-8
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
'''
def isValid(s):
    if len(s) == 0:
        return
    array = []
    for i in range(len(s)):
        if array == []:
            array.append(s[i])
            continue
        if s[i] == ']':
            if array[-1] == '[':
                array = array[:-1]
            else:
                return False
        elif s[i] == ')':
            if array[-1] == '(':
                array = array[:-1]
            else:
                return False
        elif s[i] == '}':
            if array[-1] == '{':
                array = array[:-1]
            else:
                return False
        else:
            array.append(s[i])

    if array:
        return False
    else:
        return True



print(isValid(']'))