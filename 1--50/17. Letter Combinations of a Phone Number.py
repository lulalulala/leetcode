"""Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]."""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dicts = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
                 '1': ''}
        rlist = []
        for i in digits:
            rlist.append(dicts[i])
        result = []
        if digits == '':
            return result
        for j in list(itertools.product(*rlist)):
            rstr = ''
            for k in j:
                rstr += k
            result.append(rstr)

        return result
