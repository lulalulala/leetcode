"""Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1

Example 3:

Input: [1,3,5,6], 7
Output: 4

Example 4:

Input: [1,3,5,6], 0
Output: 0

"""

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin = 0
        end = len(nums) -1
        while end - begin > 1:
            mid = (begin + end) //2
            if nums[mid] == target:
                while nums[mid] == target:
                    if mid == 0:
                        return mid
                    else:
                        mid -= 1
                return mid + 1
            elif nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                begin = mid
        if nums[begin] == target:
            return begin
        elif nums[end] == target:
            return end
        elif nums[begin] > target:
            return 0
        elif nums[end] < target:
            return len(nums)
        else:
            return end