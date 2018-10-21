"""Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        rlist = []
        list_1 = []
        self.Next(nums, list_1, rlist)
        return rlist

    def Next(self, nums, list_1, rlist):
        if not nums:
            rlist.append(list_1)
        for i in range(len(nums)):
            self.Next(nums[:i] + nums[i + 1:], list_1 + [nums[i]], rlist)
