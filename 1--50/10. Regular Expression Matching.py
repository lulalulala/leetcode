"""Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa"."""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        restr = re.search(p, s)
        if restr:
            return restr.group() == s
        else:
            return False