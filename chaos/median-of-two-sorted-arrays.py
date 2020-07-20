# coding: utf-8
'''给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
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
        index1 = 0
        index2 = 0
        m = len(nums1)
        n = len(nums2)
        total = m + n
        pre_pointer = 0
        current_pointer = 0
        while index1 < m and index2 < n:

            pre_pointer = current_pointer
            if nums1[index1] < nums2[index2]:
                current_pointer = '1:' + str(index1)
                index1 += 1
            else:
                current_pointer = '2:' + str(index2)
                index2 += 1
            print(current_pointer)
            if (index1 + index2) == (total//2) + 1:
                print(pre_pointer, current_pointer)
                break
        num1, i1 = pre_pointer.split(':')
        print(num1, i1)
        num2, i2 = current_pointer.split(':')
        i1 = int(i1)
        i2 = int(i2)
        print(num2, i2)
        i, j = 0, 0
        if num1 == '1':
            i = nums1[i1]
        else:
            i = nums2[i1]

        if num2 == '1':
            j = nums1[i2]
        else:
            j = nums2[i2]
        print(i, j)

if __name__ == '__main__':
    array1 = [1, 2, 4, 7, 8, 10]
    array2 = [3, 5, 6, 9, 11, 15, 20]
    result = Solution().findMedianSortedArrays(array1, array2)
    print(result)