"""Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4."""


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {'M': 1000, 'CM': 900, 'CD': 400, 'D': 500, 'C': 100, 'XC': 90, 'XL': 40, 'L': 50, 'X': 10, 'IX': 9,
                  'IV': 4, 'V': 5, 'I': 1}
        rint = 0
        while s != '':
            if s[:2] in romans:
                rint += romans[s[:2]]
                s = s[2:]
            else:
                rint += romans[s[:1]]
                s = s[1:]
        return rint

