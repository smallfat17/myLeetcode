#coding:utf-8

def longestPalindrome(s):
    if len(s) == 0:
        return ''

    news = '#'
    for ss in s:
        news += ss
        news += '#'
    s = news
    print(s)
    palidromes = []
    index = 1
    step = 1
    while index < len(s):

        if index - step == -1:
            palidromes.append(s[index - step + 1:index + step])
            index += 1
            step = 1
            continue
        elif index + step == len(s):
            palidromes.append(s[index - step + 1:index + step])
            print('到头了')
            break

        if s[index-step] == s[index+step]:
            step += 1
        else:
            palidromes.append(s[index - step+1:index + step])
            index += 1
            step = 1

    print(palidromes)
    max = ''
    for i in palidromes:
        if len(i) > len(max):
            max = i
    return max.replace('#','')

print(longestPalindrome("a"))




