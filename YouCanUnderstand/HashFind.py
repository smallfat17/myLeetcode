#encoding:utf-8
'''
哈希算法应用于猜词游戏
将secret和guess分别存放到两个字典中,取两者最小值
'''
#猜词游戏
def guess_secret(secret,guess):
    secret_dict = {}
    guess_dict = {}
    A = 0
    B = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            A += 1
        else:
            secret_dict[secret[i]] = secret_dict.get(secret[i],0) + 1
            guess_dict[guess[i]] = guess_dict.get(guess[i],0) + 1

    for digit in secret_dict:
        if digit in guess_dict:
            B += min(secret_dict[digit],guess_dict[digit])
    return '%dA %dB'%(A,B)

print(guess_secret('cdddad','bacdad'))