'''
给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。如果有两个数与 x 的差值一样，优先选择数值较小的那个数。

示例 1:
输入: [1,2,3,4,5], k=4, x=3
输出: [1,2,3,4]
 
示例 2:
输入: [1,2,3,4,5], k=4, x=-1
输出: [1,2,3,4]
 
说明:
k 的值为正数，且总是小于给定排序数组的长度。
数组不为空，且长度不超过 104
数组里的每个元素与 x 的绝对值不超过 104
'''

class Solution:
    def findClosestElements(self, arr, k, x):
        if len(arr) == 0:
            return
        result = []
        l = 0
        r = len(arr) - 1
        s = max(arr)
        index = 0
        while l <= r:
            mid = (l + r) // 2
            current_s = abs(arr[mid] - x)
            if current_s == 0:
                s = 0
                index = mid
                break
            if current_s < s:
                s = current_s
                index = mid
            elif current_s == s:
                if arr[mid] < arr[index]:
                    index = mid
            if arr[mid] > x:
                r = mid - 1
            else:
                l = mid + 1
        result.append(arr[index])
        k -= 1
        l = index - 1
        r = index + 1
        left_list = []
        while l>=0 and r<len(arr) and k>0:
            if abs(arr[l]-x) > abs(arr[r]-x):
                result.append(arr[r])
                r += 1
                k -= 1
            else:
                left_list.append(arr[l])
                l -= 1
                k -= 1
        left_list.reverse()
        result = left_list + result
        if k>0:
            if l < 0:
                result += arr[r:r+k]
            else:
                result = arr[l - k+1:l+1] + result
        return result


if __name__ == '__main__':
    arr = [1, 3, 6, 8]
    result = Solution().findClosestElements(arr, 1, 4)
    print(result)
