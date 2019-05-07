'''
小偷问题
     O
  O    O
O  O  O  O
子节点和父节点不可以同时偷
思路：深度遍历，计算每个节点偷与不偷值
'''
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

t = TreeNode(3)
t.left = TreeNode(4)
t.right = TreeNode(5)
t.left.left = TreeNode(1)
t.left.right = TreeNode(3)
t.right.right = TreeNode(1)

def rob(root):
    a = helper(root)
    return max(a[0],a[1])

def helper(root):
    if root == None:
        return [0,0]
    left = helper(root.left)
    right = helper(root.right)
    robValue = root.val + left[1] + right[1]
    #子节点可能偷与不偷的最大值
    skipValue = max(left[0] , left[1]) + max(right[0] , right[1])
    # print(robValue,skipValue)
    return [robValue,skipValue]

print(rob(t))


  