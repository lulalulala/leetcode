"""You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:

Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []

"""

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or len(words[0]) == 0:
            return []
        length_word = len(words[0])
        length_words = length_word * len(words)
        if length_words > len(s) or len(s) == 0:
            return []
        rlist = []
        for i in range(len(s) - length_words + 1):
            list1 = words.copy()
            n = i
            while s[i:i+length_word] in list1:
                list1.remove(s[i:i+length_word])
                i += length_word
                if len(list1) == 0:
                    rlist.append(n)
        return rlist