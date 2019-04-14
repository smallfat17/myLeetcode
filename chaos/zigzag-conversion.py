'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
'''

def convert2(s,numRows):
    if numRows == 1:
        return s
    front,tail = 0,numRows
    ss = []
    while tail<=len(s) or front <= len(s)-1:
        ss.append(s[front:tail])
        front,tail = tail - 1,tail + numRows - 1

    print(ss)
    l = []
    l.append([''] * numRows)
    l = l[0]

    for i in range(len(ss)):
        for j in range(len(ss[i])):
            if i % 2 == 0:
                l[j] += ss[i][j]
            else:
                if j >0 and j < len(ss[i]) and j < numRows-1:
                    l[numRows - j - 1] += ss[i][j]

    r = ''
    # print(l)
    for s in l:
        r += s
    return r

print(convert2('LEETCODEISHIRING',numRows=3))

