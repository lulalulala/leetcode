"""Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000

Example 2:

Input: 2.10000, 3
Output: 9.26100
"""
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:return 1
        if n < 0: return 1.0/self.myPow(x, -n)
        half = self.myPow(x, n//2)
        if n%2 == 0:
            return half * half
        else:
            return half * half * x