"""
Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = nums[0]
        y = nums[0]
        for i in range(1, len(nums)):
            if y + nums[i] < nums[i]:
                y = nums[i]
            else:
                y += nums[i]
            x = max(x, y)
        return x
