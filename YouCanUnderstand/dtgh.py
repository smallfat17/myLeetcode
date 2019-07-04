#动态规划
#爬楼梯问题  F(n) = F(n-1) + F(n-2)

#矿工挖矿问题
def gold_mining(gold_num,miner_num,gold_values,miner_needs):
    preResults = [0]*(miner_num)

    #手动遍历挖掘第一座金矿所获得的的收益情况

    for i in range(miner_num):
        #i为坐标,人数为i+1
        if i+1 < miner_needs[0]:
            preResults[i] = 0
        else:
            preResults[i] = gold_values[0]

    results = preResults.copy()

    for i in range(1,gold_num):
        for j in range(0,miner_num):
            #如果人数比挖掘当前金矿需要的人数少，则等于上一次的值
            if j+1 < miner_needs[i]:
                results[j] = preResults[j]
            else:
                t = 0 if (j - miner_needs[i]) < 0 else j - miner_needs[i] #防止出现负数
                results[j] = max(preResults[j],preResults[t]+gold_values[i])
            print(j,results)
        preResults = results[:]
        print()
    return results.pop()


gold_num = 5
miner_num = 10
gold_value = [400,500,200,300,350]
miner_needs = [5,5,3,4,3]
# print(gold_mining(gold_num,miner_num,gold_value,miner_needs))

#背包问题
def backbag_problem(W,goods,goods_weight,goods_value):
    record_map = [[0 for i in range(W+1)] for i in range(len(goods)+1)]
    #从第二行开始。所以i从1开始
    for i in range(1,len(record_map)):
        for j in range(W+1):
            if j < goods_weight[i-1]:
                record_map[i][j] = record_map[i-1][j]
            else:
                record_map[i][j] = max(record_map[i-1][j],record_map[i-1][j-goods_weight[i-1]]+goods_value[i-1])
        print(record_map)


    def show(W,goods,goods_weight,record_map):
        print('max value:',record_map[len(goods)][W])
        x = [False for i in range(len(goods)+1)]
        i = len(goods)
        j = W
        while i >= 0:
            if record_map[i][j] > record_map[i-1][j]:
                x[i] = True
                j -= goods_weight[i-1]
            i -= 1
        print('choices are ')
        for i in range(len(x)):
            if x[i]:
                print(i)

    show(W,goods,goods_weight,record_map)

W = 8
goods = ['a','b','c','d']
goods_weight = [2,4,5,3]
goods_value = [5,4,6,2]
# print(backbag_problem(W,goods,goods_weight,goods_value))




