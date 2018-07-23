'''Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        runner1 = runner2 = head
        for i in range(n):
            runner1 = runner1.next
        # 让runner1与runner2拉开n个间距，当runner1先跑完时runner2在倒数第n个前
        if runner1 == None:
            return runner2.next
        while runner1.next:
            runner1 = runner1.next
            runner2 = runner2.next
        runner2.next = runner2.next.next
        return head
