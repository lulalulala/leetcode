"""Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321

Note:
Assume we are dealing with an environment which could only store
integers within the 32-bit signed integer
range: [−231,  231 − 1]. For the purpose of this problem, assume
that your function returns 0 when the reversed integer overflows."""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)
        if x < 0:
            x_str = '-' + str(abs(x))[::-1]
        else:
            x_str = x_str[::-1]
        x_int = int(x_str)
        if x_int < (-2**31) or x_int > (2**31 - 1):
            x_int = 0
        return x_int