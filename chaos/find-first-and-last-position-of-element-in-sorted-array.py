'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

解法
    二分法找到一个target在数组中的位置，如果不存在返回[-1, -1]
    如果存在
        向左边使用二分查找，找到第一个为target的元素，返回下标，
        向右边使用二分查找，找到最后一个为target的元素，返回下标
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        res_l = -1
        res_r = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right) // 2
            if target == nums[mid]:
                res_l = self.bi_search_left(nums, target, mid)
                res_r = self.bi_search_right(nums, target, mid)
                break
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return [res_l, res_r]

    def bi_search_left(self, nums, target, index):
        left, right = 0, index
        result = 0
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return result

    def bi_search_right(self, nums, target, index):
        result = index
        left, right = index + 1, len(nums) - 1
        print('index: ', index)
        while left <= right:
            mid = (left + right) // 2
            print('mid: ', mid)
            if nums[mid] == target:
                result = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return result





if __name__ == '__main__':
    nums = [5, 7, 7, 7, 7, 8, 8, 8, 10, 10, 10, 11, 12]
    result = Solution().searchRange(nums, 10)
    print(result)