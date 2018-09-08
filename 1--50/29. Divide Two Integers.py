"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3

Example 2:

Input: dividend = 7, divisor = -3
Output: -2

Note:

    Both dividend and divisor will be 32-bit signed integers.
    The divisor will never be 0.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

"""


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        isPositive = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            isPositive = -1
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor:
            return 0
        reint = 0
        while dividend >= divisor:
            i = 1
            n = divisor
            while n << 2 < dividend:
                i <<= 2
                n <<= 2
            reint += i
            dividend -= n

        reint = isPositive * reint
        MAX_INT = 2147483647
        if reint > MAX_INT:
            return MAX_INT
        return reint