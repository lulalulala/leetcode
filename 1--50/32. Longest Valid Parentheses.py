"""Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

"""


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        rlist = []
        left, right = '(', ')'
        for i, n in enumerate(s):
            if n == left:
                rlist.append(i)
            elif n == right:
                if not rlist:
                    rlist.append(i)
                else:
                    if s[rlist[-1]] == left:
                        rlist.pop()
                    else:
                        rlist.append(i)

        if not rlist:
            return len(s)
        rlist.append(len(s))
        rlist.insert(0, -1)
        m = []
        for i in range(1, len(rlist)):
            n = rlist[i] - rlist[i - 1] - 1
            m.append(n)
        return max(m)