"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0
        last = len(nums) - 1

        while first <= last:
            mid = (first + last) // 2
            if target == nums[mid]:
                return mid

            elif target < nums[mid]:
                if nums[first] < nums[mid]:
                    if target >= nums[first]:
                        last = mid - 1
                    else:
                        first = mid + 1
                elif nums[first] > nums[mid]:
                    last = mid - 1
                elif nums[first] == nums[mid]:
                    first = mid + 1

            elif target > nums[mid]:
                if nums[first] < nums[mid]:
                    first = mid + 1
                elif nums[first] > nums[mid]:
                    if target >= nums[first]:
                        last = mid - 1
                    else:
                        first = mid + 1
                elif nums[first] == nums[mid]:
                    first = mid + 1
        return -1