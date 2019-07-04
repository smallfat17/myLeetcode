'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
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
                self.helper(candidates, target, nums)
        return self.result

    def helper(self, candidates, target, nums):
        for i in range(len(candidates)):
            # print(nums, candidates[i])
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
                if self.helper(candidates, target, new_nums):
                    return True



if __name__ == '__main__':
    candidates = [2,5,2,1,2]
    target = 5
    so = Solution()
    result = so.combinationSum(candidates, target)
    print(result)
