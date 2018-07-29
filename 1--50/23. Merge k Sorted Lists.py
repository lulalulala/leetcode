"""Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        rdict = {}
        rlink = runner = ListNode(0)
        for rlist in lists:
            while rlist != None:
                if rlist.val in rdict:
                    rdict[rlist.val] += 1
                else:
                    rdict[rlist.val] = 1
                rlist = rlist.next

        for key in sorted(rdict.keys()):
            for i in range(rdict[key]):
                runner.next = ListNode(key)
                runner = runner.next
        return rlink.next
