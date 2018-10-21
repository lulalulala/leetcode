"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Note:

    The length of both num1 and num2 is < 110.
    Both num1 and num2 contain only digits 0-9.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        dict_1 = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "0":0}
        dict_2 = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 0:"0"}
        l_num1 = len(num1)
        l_num2 = len(num2)
        i_num1 = 0
        for i in num1:
            i_num1 += dict_1[i]*10**(l_num1-1)
            l_num1-=1
        i_num2 = 0
        for n in num2:
            i_num2 += dict_1[n]*10**(l_num2-1)
            l_num2 -= 1
        x = i_num1*i_num2
        if x == 0:
            return "0"
        rstr = ""
        while x > 0:
            y = x % 10
            rstr = dict_2[y] + rstr
            x //= 10
        return rstr