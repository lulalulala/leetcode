"""
Given an array of strings, group anagrams together.
Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        rlist = []
        for i in strs:
            n = list(i)
            n.sort()
            rlist.append(n)
        rlist_1 = enumerate(rlist)
        list_1 = []
        list_2 = []
        for key in rlist_1:
            if key[1] not in list_1:
                list_1.append(key[1])
                list_2.append([strs[key[0]]])
            else:
                for m in range(len(list_1)):
                    if list_1[m] == key[1]:
                        list_2[m].append(strs[key[0]])
        return list_2