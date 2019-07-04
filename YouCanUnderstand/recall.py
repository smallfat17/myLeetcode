#回溯算法

#经典例题-----遍历所有排列方式
class Solution():
    def solve_permutation(self,array):
        if len(array) == 0:
            return []
        self.helper(array,[])

    def helper(self,array,solution):
        if len(array) == 0:
            print(solution)
            return
        for i in range(len(array)):
            newSolution = solution + [array[i]]
            newArray = array[:i] + array[i+1:]
            self.helper(newArray,newSolution)

yellows = ['红','黄','绿','蓝']
# Solution().solve_permutation(yellows)

#排列组合问题
class Solution2():
    def solve_permutation(self,array,n):
        if len(array) == 0:
            return []
        self.helper(array,n,[])

    def helper(self,array,n,solution):
        if len(solution) == n:
            print(solution)
            return
        for i in range(len(array)):
            newSolution = solution + [array[i]]
            newArray = array[i+1:]
            self.helper(newArray,n,newSolution)

yellows = ['红','黄','绿','蓝']
# Solution2().solve_permutation(yellows,2)

#找单词问题
class Solution3():
    '''

    '''
    def __init__(self):
        self.directions = [[1,0],[0,1],[-1,0],[0,-1]]

    def word_search(self,board,word):
        if word == '':
            return True
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    board[row][col] = ''
                    if self.helper(board,word[1:],row,col):
                        return True
        return False

    def helper(self,board,newWord,row,col):
        if newWord == '':
            return True
        for direction in self.directions:
            newRow = row+direction[0]
            newCol = col+direction[1]
            if newRow >= 0 and newRow < len(board) and newCol >= 0 and newCol < len(board[0]):
                if board[newRow][newCol] == newWord[0]:
                    if self.helper(board,newWord[1:],newRow,newCol):
                        return True

board = [
    ['h','e','l','l','o'],
    ['i','w','e','e','h'],
    ['m','e','h','k','b'],
    ['s','f','a','t','d']
]

# print(Solution3().word_search(board=board,word='fat'))

#八个皇后问题。要求在每一列每一行跟每一条斜线有且只有一个皇后
class Solution4():
    def legal_quene(self,n):
        self.helper([0]*n,0,n)
    def helper(self,array,rowIndex,n):
        if rowIndex == n:
            print(array)
            return
        for i in range(n):
            array[rowIndex] = i
            if self.is_valid(array,rowIndex,n):
                self.helper(array,rowIndex+1,n)

    def is_valid(self,array,rowIndex,n):
        for i in range(rowIndex):
            if array[i] == array[rowIndex]:
                return False
            if abs(array[i] - array[rowIndex]) == rowIndex - i:
                return False
        return True

# s = Solution4()
# s.legal_quene(8)

class Solution5():
    def solve_sudoku(self,board):
        self.helper(board,0,0)


    def helper2(self,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    continue
                for num in range(1, 10):
                    if self.is_valid(board, i, j, num):
                        board[i][j] = str(num)
                        if self.helper2(board): return True
                        board[i][j] = "."
                return False
        return True


    def helper(self,board,row,col):
        if row == 9:
            # print(board)
            return True
        if board[row][col] == ".":
            for num in range(1,10):
                if self.is_valid(board,row,col,num):
                    board[row][col] = str(num)
                    if col == 8:
                        if self.helper(board,row+1,0): return True
                    else:
                        if self.helper(board,row,col+1): return True
                    board[row][col] = "."
            return False
        else:
            if col == 8:
                if self.helper(board, row + 1, 0): return True
            else:
                if self.helper(board, row, col + 1): return True

    # def is_valid(self,board,row,col,n):
    #     for i in range(9):
    #         if board[row][i] == n: return False
    #         if board[i][col] == n: return False
    #         if board[row // 3 * 3 + i / 3][col // 3 * 3 + i % 3] == n: return False
    #     return True

    def is_valid(self,board,row,col,num):
        # print(row,col)
        num = str(num)
        if num in board[row]:
            return False
        if num in [current[col] for current in board]:
            return False
        block_x = row // 3
        block_y = col // 3
        block = [board[i][j] for i in range(block_x*3,(block_x+1)*3) for j in range(block_y*3,(block_y+1)*3)]
        if num in block:
            return False
        return True


sudo = [
    [4,1,0,0,0,7,8,5,0],
    [8,0,6,0,0,0,0,0,9],
    [0,2,0,0,9,0,6,0,0],
    [0,0,4,0,0,0,0,1,2],
    [2,0,0,5,8,0,0,7,0],
    [0,0,0,0,0,0,5,0,0],
    [0,0,0,7,0,2,0,0,0],
    [0,0,8,0,1,0,0,0,0],
    [0,7,0,0,6,0,0,0,0]
]

sudo2 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]

print(Solution5().solve_sudoku(sudo2))

#判断数独是否合理
class Solution6():
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                else:
                    if not self.is_valid(board, i, j, board[i][j]):
                        print(i, j)
                        return False
        return True

    def is_valid(self, board, row, col, num):
        if board[row].count(num) >= 2:
            return False
        if [current[col] for current in board].count(num) >= 2:
            return False
        block_x = row // 3
        block_y = col // 3
        block = [board[i][j] for i in range(block_x * 3, (block_x + 1) * 3) for j in
                 range(block_y * 3, (block_y + 1) * 3)]
        if block.count(num) >= 2:
            return False
        return True

sudo = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

# print(Solution6().isValidSudoku(sudo))

