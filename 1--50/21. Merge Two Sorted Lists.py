"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rlist = runner = ListNode(0)
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        while l1 and l2:
            if l1.val >= l2.val:
                runner.next = l2
                l2 = l2.next
            else:
                runner.next = l1
                l1 = l1.next
            runner = runner.next
        while l1:
            runner.next = l1
            l1 = l1.next
            runner = runner.next
        while l2:
            runner.next = l2
            l2 = l2.next
            runner = runner.next
        return rlist.next