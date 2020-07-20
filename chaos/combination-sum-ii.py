'''给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
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
    def combinationSum2(self, candidates, target):
        self.results = []
        for i in range(len(candidates)):
            self.helper(candidates[:i]+candidates[i+1:], target, array=[candidates[i]],)
        return self.results

    def helper(self, candidates, target, array=None):
        if not array:
            array = []
        print('array', array)
        if sum(array) == target:
            self.results.append(array)
            return True
        if sum(array) > target:
            return
        for i in range(len(candidates)):
            new_array = array[:]
            new_array.append(candidates[i])
            if self.helper(candidates[:i] + candidates[i+1:], target, new_array):
                break

if __name__ == '__main__':
    print(Solution().combinationSum2([2,5,2,1,2], 5))