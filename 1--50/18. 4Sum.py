"""Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                m, n = j + 1, len(nums) - 1
                while m < n:
                    sum = nums[i] + nums[j] + nums[m] + nums[n]
                    if sum == target:
                        sum_list = [nums[i], nums[j], nums[m], nums[n]]
                        if sum_list not in result:
                            result.append(sum_list)
                        m += 1
                        n -= 1
                    if sum < target:
                        m += 1
                    elif sum > target:
                        n -= 1
        return result
