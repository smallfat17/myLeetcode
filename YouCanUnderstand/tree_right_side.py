class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None



import queue
#层次遍历---队列--广度优先遍历经典应用场景
def level_read(t):
    if t == None:
        return None

    q = queue.Queue()
    q.put(t)
    results = ''
    while not q.empty():
        current = q.get()
        results += str(current.val)
        if current.left != None: q.put(current.left)
        if current.right !=None: q.put(current.right)
    return results

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
t.right.left = TreeNode(6)
t.right.right = TreeNode(7)

print(level_read(t))