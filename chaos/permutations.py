'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution(object):
    def __init__(self):
        self.results = []
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return
        self.helper(nums, [])

        return self.results

    def helper(self, nums, solution):
        if len(nums) == 0:
            if solution not in self.results:
                self.results.append(solution)
            return
        for i in range(len(nums)):
            new_solution = solution + [nums[i]]
            new_nums = nums[:i] + nums[i+1:]
            self.helper(new_nums, new_solution)


if __name__ == '__main__':
    result = Solution().permute([1,1,3])
    print(result)
