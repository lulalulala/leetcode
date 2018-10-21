"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

"""


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height == []:
            return 0
        h = max(height)
        y = 0
        for x in height:
            if x == h:
                y += 1
        n = 0
        m = 0
        for i in range(len(height)):
            if height[i] == h:
                n += 1
                if n == y:
                    m = i
                    break
        num1 = self.nums(height[:m + 1])
        list_2 = height[m:]
        num2 = self.nums(list_2[::-1]) + num1
        return num2

    def nums(self, height):
        left = 0
        num = 0
        m = 0
        n = 0
        for i in range(len(height)):
            if height[i] > left:
                left = height[i]
            else:
                num += left - height[i]
        return num