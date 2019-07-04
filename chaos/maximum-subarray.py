'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

'''

#分治
class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) // 2
        leftSum = self.maxSubArray(nums[:mid])
        rightSum = self.maxSubArray(nums[mid:])
        leftMiddleSum = 0
        rightMiddleSum = 0
        maxLeft = 0
        maxRight = 0
        for i in range(mid - 1,-1,-1):
            leftMiddleSum += nums[i]
            maxLeft = max(leftMiddleSum, maxLeft)
        for j in range(mid+1,len(nums), 1):
            rightMiddleSum += nums[j]
            maxRight = max(rightMiddleSum, maxRight)
        return max(leftSum, maxLeft+nums[mid]+maxRight, rightSum)

    #动态规划
    def maxSubArray2(self, nums):
        if len(nums) == 0:
            return
        max_sum = nums[0]
        temp = nums[0]
        for num in nums[1:]:
            if temp < 0:
                temp = num
            else:
                temp += num
            max_sum = max(max_sum, temp)
        return max_sum


if __name__ == '__main__':
    result = Solution().maxSubArray2([-2,1,-3,4,-1,2,1,-5,4])
    print(result)
