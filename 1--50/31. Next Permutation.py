"""Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = -1
        if len(nums) <= 1:
            return
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                n = i
                break

        if n == -1:
            nums.sort()
        else:
            m = len(nums) - 1
            while m > 0:
                if nums[m] > nums[n]:
                    nums[m], nums[n] = nums[n], nums[m]
                    nums[n + 1:] = sorted(nums[n + 1:])
                    break
                m -= 1