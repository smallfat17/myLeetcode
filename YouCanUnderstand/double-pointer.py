#coding:utf-8
'''
双指针问题
 例1：合并两个有序数组
'''

def combineToSortedList(list1,list2):
    index = 0
    ans = list1.copy()
    for i in range(0,len(list2)):
        while index < len(list1):
            if  list2[i] <= list1[index]:
                ans.insert(index+i,list2[i])
                break
            else:
                index += 1
    else:
        ans = ans + list2[i:]
    return ans

# print(combineToSortedList([1,2,5,6],[3,4]))

def combineToSortedList2(list1,list2):
    index1 = 0
    index2 = 0
    l = []
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] > list2[index2]:
            l.append(list2[index2])
            index2 += 1
        else:
            l.append(list1[index1])
            index1 += 1
    if index1 <len(list1):
        l = l + list1[index1:]
    elif index2 < len(list2):
        l = l + list2[index2:]

    return l


# combineToSortedList2([1,2,5,6],[3,4])

#二分查找
flag = False
def twosearch(nums,target):
    head,tail = 0,len(nums)
    while tail - head > 1:
        mid = (tail+head) // 2
        print(nums[mid])
        if nums[mid] > target:
            tail = mid
        elif nums[mid] < target:
            #解决偶数长度
            head = mid + 1
        elif nums[mid] == target:
            return True
    if nums[head] == target:
        return True
    else:
        return False

# print(twosearch([1,3,4,6,8,11,14],14))

#双指针查找两数之和
#需要排序。费时
def twoSum(nums,target):
    nums.sort()

    if len(nums) == 0:
        return False

    head,tail = 0,len(nums)-1
    while head < tail:
        sum = nums[head] + nums[tail]
        if sum > target:
            tail -= 1
        elif sum < target:
            head += 1
        elif sum == target:
            return True
    return False

# print(twoSum([1,7,5,2],3))

#哈希查找算法

def twoSum_hash(nums,target):
    if len(nums) == 0:
        return False

    d = {}
    for i in range(len(nums)):
        current = nums[i]
        if (target - current) in d:
            return True
        else:
            d[current] = target - current
    return False

print(twoSum_hash([1111,1,1,1,1],3))