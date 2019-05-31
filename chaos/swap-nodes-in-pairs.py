#coding:utf-8
'''
反转链表I
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.


反转链表II
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明:
1 ≤ m ≤ n ≤ 链表长度。
示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
#反转链表I
def reverseList(head):
    pre = None
    current = head
    while current:
        next = current.next
        current.next = pre
        pre = current
        current = next
    return pre

#反转链表II
def reverseList2(head,m,n):
    pre = None
    current = head
    notReverse = head
    reverseTail = None
    temp = None
    index = 1
    while index <= n:
        if index < m:
            index += 1
            current = current.next
            temp = notReverse
            notReverse = notReverse.next
            continue
        if index == m:
            reverseTail = current
        next = current.next
        current.next = pre
        pre = current
        current = next

        index += 1
    if temp:
        temp.next = pre
    else:
        head = pre
    reverseTail.next = current
    return head

reverseL = reverseList2(l,2,4)


while reverseL:
    print(reverseL.val)
    reverseL = reverseL.next


