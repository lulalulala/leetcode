"""Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4."""


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romans = [["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
                  ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
                  ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
                  ["M", "MM", "MMM"]]
        rstr = ''
        i = 0
        while num > 0:
            if num % 10 > 0:
                rstr = romans[i][num % 10 - 1] + rstr
            i += 1
            num = num // 10
        return rstr
