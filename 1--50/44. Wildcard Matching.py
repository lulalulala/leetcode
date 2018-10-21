"""Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
Note:
    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
"""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i, j, s_star, p_star = 0, 0, 0, -1
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == "?"):
                i, j = i+1, j+1
            elif j < len(p) and p[j] == "*":
                s_star, p_star = i, j
                j += 1
            elif p_star != -1:
                s_star += 1
                i, j = s_star, p_star+1
            else:
                return False
        while j < len(p) and p[j] == "*":
            j += 1
        return True if j == len(p) else False