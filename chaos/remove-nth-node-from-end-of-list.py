'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)


def removeNthFromEnd( head, n):
    if not head or not head.next:
        return None
    headNode = head
    tailNode = head
    index = 0
    while tailNode.next:
        if index >= n :
            headNode = headNode.next
        tailNode = tailNode.next
        index += 1
    if index < n:
        return head.next
    else:
        headNode.next = headNode.next.next
    return head

# removeNthFromEnd(l,3)


def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return head
    headnode = head.next

    return headnode


#反转链表
def reverseList(head):
    pre = None
    current = head
    while current:
        next = current.next
        current.next = pre
        pre = current
        current = next
    return pre
ll = reverseList(l)
while ll:
    print(ll.val)
    ll = ll.next

