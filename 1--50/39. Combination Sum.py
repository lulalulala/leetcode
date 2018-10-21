"""Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

"""

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def rSum(candidates, target, rlist_1, rlist):
            for i in range(len(candidates)):
                n = target
                m = n-candidates[i]
                if m > 0:
                    rlist_2 = rlist_1.copy()
                    rlist_2.append(candidates[i])
                    rSum(candidates[i:],m,rlist_2, rlist)
                elif m < 0:
                    break
                else:
                    rlist_2 = rlist_1.copy()
                    rlist_2.append(candidates[i])
                    rlist.append(rlist_2)
                    return
        candidates.sort()
        rlist_1 = []
        rlist = []
        rSum(candidates, target, rlist_1, rlist)

        return rlist