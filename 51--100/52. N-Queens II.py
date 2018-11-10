"""Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]"""


class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        rlist, list_1 = [], []
        self.rint = 0
        n_0 = n
        self.NQueens(list_1, n, n_0)
        return self.rint

    def NQueens(self, list_1, n, rn_0):
        # rint += 1
        if rn_0 == 0:
            self.rint += 1
        for i in range(n):
            rnum = 10 ** i
            rlist_1 = list_1[:]
            rlist_1.append(rnum)
            if self.legal_Queens(rlist_1, n):
                self.NQueens(rlist_1, n, rn_0 - 1)

    def legal_Queens(self, list_1, n):
        if list_1 != [] and list_1:
            x = len(list_1)
            n = list_1[x - 1]
            if x == 1:
                return True
            else:
                for y in range(x - 1):
                    m = list_1[y]
                    if m == n or m / n == 10 ** (x - 1 - y) or n / m == 10 ** (x - 1 - y):
                        return False
        return True
