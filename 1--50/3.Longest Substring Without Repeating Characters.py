#Given "abcabcbb", the answer is "abc", which the length is 3.

#Given "bbbbb", the answer is "b", with the length of 1.

#Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_str = ''
        len_str = 0
        for n in s:
            if n in sub_str:
                if len(sub_str) > len_str:
                    len_str = len(sub_str)
                sub_str = sub_str[sub_str.find(n) + 1:] + n
            else:
                sub_str += n

        if len(sub_str) > len_str:
            len_str = len(sub_str)

        return len_str