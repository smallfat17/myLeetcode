'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0 and len(nums1) == 0:
            return
        def half_search(nums, target):
            l = 0
            r = len(nums) - 1
            s = max(nums)
            index = 0
            while l <= r:
                mid = (l + r) // 2
                current_s = abs(nums[mid] - target)
                if current_s < s:
                    index = mid
                    s = current_s
                if nums[mid] == target: return mid
                if nums[mid] < target: l = mid + 1
                else: r = mid - 1
            return index

        len1 = len(nums1)
        len2 = len(nums2)
        middle_len = (len1 + len2) // 2
        left = 0
        right = len1 - 1
        while left <= right:
            mid = (left + right) // 2
            closest_index= half_search(nums2, nums1[mid])
            print(nums1[mid], nums2[closest_index])
            if nums1[mid] < nums2[closest_index]:
                current_middle_len = mid  + closest_index
            else:
                current_middle_len = mid + closest_index + 1
            print('current_middle', str(current_middle_len))
            print(middle_len)
            if current_middle_len == middle_len:
                return nums1[mid]
            elif current_middle_len == middle_len + 2:
                # if nums1[mid] > nums2[closest_index]:
                return (nums1[mid] + nums2[closest_index]) / 2
            elif current_middle_len > middle_len:
                right = mid - 1
            else:
                left = mid + 1

        return nums1[mid]



if __name__ == '__main__':
    result = Solution().findMedianSortedArrays([1, 3],[2])
    print(result)
