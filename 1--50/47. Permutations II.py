"""Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        list_1, list_2 = [], []
        self.permutations(nums, list_1, list_2)
        return list_2

    def permutations(self, nums, list_1, list_2):
        if len(nums) == 0:
            list_2.append(list_1)
        for i in range(len(nums)):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            self.permutations(nums[:i] + nums[i + 1:], list_1 + [nums[i]], list_2)