"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def gP(n, left, right, rstr, rlist):
            if len(rstr) == 2 * n:
                if right == 0:
                    rlist.append(rstr)
                return
            if left < 0 or right > n or right < 0:
                return
            gP(n, left - 1, right + 1, rstr + "(", rlist)
            gP(n, left, right - 1, rstr + ")", rlist)

        rlist = []
        gP(n, n, 0, '', rlist)
        return rlist
