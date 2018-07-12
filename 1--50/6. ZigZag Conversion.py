"""Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        row = 0
        step = 1
        rstr = ['' for i in range(numRows)]
        if numRows == 1:
            return s

        for i in s:
            if row == 0:
                step = 1
            if row == numRows - 1:
                step = -1
            rstr[row] += i
            row += step
        return ''.join(rstr)
