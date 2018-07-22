"""Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        rlist = []

        for i in range(len(nums) - 2):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue

            for n in range(i + 1, len(nums) - 1):
                x = -1 * (nums[i] + nums[n])
                list1 = nums[n + 1:]

                if x in nums[n + 1:]:
                    list2 = sorted([nums[i], nums[n], x])
                    if list2 not in rlist:
                        rlist.append(list2)
        return rlist
