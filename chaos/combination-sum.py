'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]

示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

class Solution:
    def __init__(self):
        self.result = []

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return None
        for i in range(len(candidates)):
            nums = [candidates[i], ]
            if candidates[i] == target:
                self.result.append(nums)
            else:
                self.helper(candidates[i:], target, nums)
        return self.result

    def helper(self, candidates, target, nums):
        for i in range(len(candidates)):
            print(nums, candidates[i])
            temp = sum(nums) + candidates[i]
            if temp == target:
                new_nums = nums.copy()
                new_nums.append(candidates[i])
                self.result.append(new_nums)
                return True
            elif temp > target:
                continue
            else:
                new_nums = nums.copy()
                new_nums.append(candidates[i])
                self.helper(candidates[i: ], target, new_nums)


if __name__ == '__main__':
    candidates = [4, 2 ,8]
    target = 8
    so = Solution()
    result = so.combinationSum(candidates, target)
    print(result)
    # c = candidates.copy()
    # print(candidates)

