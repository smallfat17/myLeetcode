#贪心算法

#找零问题
def get_change(money):
    par = [0.05,0.1,0.2,0.5,1.0,2.0]
    sum = money
    index = len(par) - 1
    while index >= 0:
        if sum >= par[index]:
            n = sum // par[index]
            sum = float('%.6f' % (sum - par[index]*n))
            print(int(n),par[index])
        index -= 1

print(get_change(6.05))
