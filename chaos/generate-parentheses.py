'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

#回溯法

def generateParenthesis(n):
    '''
    如果左边的'('少于 n ，可以继续添加'('    ---->一共n对
    如果右边的')' 少于左边的 '(' ,则可以在右边添加')'
    '''
    ans = []
    def track(S='',left=0,right=0):
        if len(S) == 2 * n:
            ans.append(S)
        if left < n:
            track(S+'(',left+1,right)
        if left > right:
            track(S+')',left,right+1)
    track()
    return ans

print(generateParenthesis(3))