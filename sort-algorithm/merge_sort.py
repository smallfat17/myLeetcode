'''
归并排序
'''
def merge_sort(nums):
    # print(nums)
    if len(nums) == 0:
        return
    if len(nums) == 1:
        return [nums[0]]
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    new_list = []
    l_index = 0
    r_index = 0
    while l_index < len(left)  and r_index < len(right):
        if left[l_index] > right[r_index]:
            new_list.append(right[r_index])
            r_index += 1
        else:
            new_list.append(left[l_index])
            l_index += 1

    new_list.extend(left[l_index:])
    new_list.extend(right[r_index:])

    print(new_list)
    return new_list




if __name__ == '__main__':
    nums = [4,7,9,1,2,6,5]
    l = merge_sort(nums)
    print(l)