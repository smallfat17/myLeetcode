'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # print(nums[mid])
            print(nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[0]:
                r = mid - 1
            elif nums[mid] > nums[-1]:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1

if __name__ == '__main__':
    nums = [3, 5, 1]
    result = Solution().search(nums, 3)
    print(result)