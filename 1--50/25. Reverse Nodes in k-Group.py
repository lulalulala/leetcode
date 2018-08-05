"""Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

    Only constant extra memory is allowed.
    You may not alter the values in the list's nodes, only nodes itself may be changed.

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        number = 0
        i = head
        while i is not None:
            i = i.next
            number += 1

        def nodelist(node, k):
            runner1 = None
            runner0 = runner2 = runner3 = node
            for x in range(k):
                runner2 = runner3.next
                runner3.next = runner1
                runner1 = runner3
                runner3 = runner2
            return (runner0, runner1, runner2)

        if number < k:
            return head
        if k == 1:
            return head
        node_head = nodelist(head, k)
        head = node_head[1]
        runner4 = node_head[0]
        for n in range(number // k - 1):
            node_head = nodelist(node_head[2], k)
            runner4.next = node_head[1]
            runner4 = node_head[0]
        node_head[0].next = node_head[2]
        return head
