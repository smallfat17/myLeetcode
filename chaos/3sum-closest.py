#coding:utf-8
'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

解题思路：
    遍历每个元素,采用双指针 head = i +1 .tail = len(nums) - 1
                如果sum大于target  tail - 1   大于小于比较绝对值
                else sum 小于target head + 1
'''


def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    nums.sort()

    result = nums[0]+nums[1]+nums[2]
    for i in range(len(nums)):
        head, tail = i+1, len(nums)-1

        while head < tail:
            sum = nums[i] + nums[head] + nums[tail]
            if abs(sum - target) < abs(result - target):
                result = sum
            if sum == target:
                return sum
            elif sum > target:
                tail -= 1
            elif sum < target:
                head += 1
    return result

