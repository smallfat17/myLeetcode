import collections
dict

'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
示例 1:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
'''


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = [matrix[0][0]]
        m = 0
        n = 0
        max_m = len(matrix)
        max_n = len(matrix[0])
        round = 0
        direction = 1
        while len(result) < len(matrix)*len(matrix[0]):
            print(m,n)
            if n >= round and n < max_n - 1:
                n += direction

            elif n == max_n - 1:
                if m == max_n - 1:
                    n -= 1
                    direction = -1
                    round += 1
                else:
                    m += 1

            result.append(matrix[m][n])
        return  result


if __name__ == '__main__':
    matrix = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    result = Solution().spiralOrder(matrix)
    print(result)