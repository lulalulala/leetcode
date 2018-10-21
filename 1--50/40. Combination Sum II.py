"""Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

"""


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        list_1 = []
        rlist = []
        rnumber = 0
        self.Sum3(candidates, target, rnumber, list_1, rlist)
        return rlist

    def Sum3(self, candidates, target, rnumber, list_1, rlist):
        for i in range(len(candidates)):
            rnumber1 = rnumber + candidates[i]
            list_3 = list_1.copy()
            list_3.append(candidates[i])
            if rnumber1 < target:
                self.Sum3(candidates[i + 1:], target, rnumber1, list_3, rlist)
            elif rnumber1 > target:
                break
            else:
                if list_3 not in rlist:
                    rlist.append(list_3)
                    return