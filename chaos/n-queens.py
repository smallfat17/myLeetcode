'''
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
'''
from time import perf_counter
class Solution(object):
    def __init__(self):
        self.results = []
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        p0 = perf_counter()
        self.helper([-1]*n, 0, n)
        print(perf_counter() - p0)
        return self.results

    def helper(self, positionList, rowNum, n):
        if rowNum == n:
            self.results.append(positionList.copy())
            return True
        for i in range(n):
            positionList[rowNum] = i
            if self.isValid(positionList, rowNum):
                self.helper(positionList, rowNum+1, n)

    def isValid(self, positionList, rowNum):
        for i in range(rowNum):
            if positionList[i] == positionList[rowNum]:
                return False
            elif abs(positionList[i] - positionList[rowNum]) == rowNum - i:
                return False
        return True


if __name__ == '__main__':
    result = Solution().solveNQueens(8)
    print(result)
