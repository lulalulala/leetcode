"""Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2."""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        relist = []
        x = 0
        y = len(height) - 1
        while x < y:
            if height[x] < height[y]:
                relist.append(height[x]*(y-x))
                x += 1
            else:
                relist.append(height[y]*(y-x))
                y -= 1
        return max(relist)
