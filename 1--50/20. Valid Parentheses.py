"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dicts = {'{':'}', '[':']', '(':')'}
        rlist = []
        for i in s:
            if i in dicts:
                rlist.append(i)
            elif not rlist or i != dicts[rlist.pop()]:
                return False
        return not rlist