import sys
sys.setrecursionlimit(100000)

def sumSubarrayMins(A):
    if len(A) == 0:
        return 0
    l = []

    def get_children(a, index):
        l.append(a)
        if index < len(A):
            newa = a[:]
            newa.append(A[index])
            get_children(newa, index + 1)

    for i in range(len(A)):
        current = [A[i]]
        get_children(current, i + 1)

    result = 0
    for j in l:
        result += min(j)
    return result
# A = [3,1,2,4]
# print(sumSubarrayMins(A))

def sumSubarrayMins2(A):
    if len(A) == 0:
        return 0
    num_array_list = [0] * len(A)
    for i in range(len(A)):
        stack = []
        for j in range(i,len(A)):
            if len(stack) == 0:
                stack.append(A[i])
            if stack[-1] > A[j]:
                num_array_list[i] += A[j]
                stack.pop(-1)
                stack.append(A[j])
            else:
                num_array_list[i] += stack[-1]
    return sum(num_array_list) % (10 ** 9 + 7)

print(sumSubarrayMins2(A))

