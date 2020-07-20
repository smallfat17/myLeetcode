'''
归并排序
'''
def merge_sort(nums):
    # print(nums)

    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(left, right):
    new_list = []
    l_index = 0
    r_index = 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index][0] > right[r_index][0]:
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
    nums =  [[74,78],[61,63],[46,50],[51,54],[50,50],[60,64],[39,42],[25,27],[91,95]]
    l = merge_sort(nums)
    print(l)