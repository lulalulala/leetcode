"""Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        if x_str[::-1] == x_str:
            return True
        else:
            return False