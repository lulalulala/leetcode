"""Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]."""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        if len(nums) <= 1:
            return dict
        for i in len(nums):
            if nums[i] in dict:
                return [dict[nums[i]],i]
            else:
                dict[target - nums[i]] = i
