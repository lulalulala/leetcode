"""Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2
        nums3 = sorted(nums3)
        if len(nums3)%2 == 1:
            median = nums3[len(nums3)//2]
        else:
            n = int(len(nums3)/2)
            n2 = nums3[n-1] + nums3[n]
            median = n2/2
        return median


