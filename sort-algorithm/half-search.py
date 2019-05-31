
#二分查找
def half_search(l,target):
    if len(l) == 0:
        return False
    head = 0
    tail = len(l) - 1
    while tail >= head:
        print(head,tail)
        mid = (head + tail) // 2
        if l[mid] > target:
            tail = mid - 1
        elif l[mid] < target:
            head = mid + 1
        else:
            print(mid)
            return True
    return False


l = [1,3,5,6]
target = 7
print(half_search(l,target))