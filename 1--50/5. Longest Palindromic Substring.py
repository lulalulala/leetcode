"""Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb" """


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        list1 = []
        list2 = []
        log_str = ''
        for i in s:
            if i not in list1:
                list1.append(i)
            else:
                list2.append(i)
        if list2 == []:
            log_str = s[0]
        for n in list2:
            x1 = s.find(n)
            x2 = len(s) - 1 - s[::-1].find(n)
            str_out = s[x1:x2 + 1]
            if len(str_out) > len(log_str):
                log_str = str_out
        return log_str
