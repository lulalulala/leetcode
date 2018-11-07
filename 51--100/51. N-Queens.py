"""Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        rlist, rlist_1 = [], []
        n_0 = n
        self.NQueens(rlist_1, rlist, n, n_0)
        return rlist

    def NQueens(self, rlist_1, rlist, n, rn_0):
        if rn_0 == 0:
            rlist.append(rlist_1)
        for i in range(n):
            list_1 = rlist_1[:]  # 注意copy原列表，防止修改原列表
            n_0 = n - rn_0
            rstr = '.' * i + 'Q' + '.' * (n - 1 - i)
            list_2 = [i, n_0]
            list_1.append(rstr)
            if self.is_legal(list_2, list_1, n, rlist):
                self.NQueens(list_1, rlist, n, rn_0 - 1)

    def is_legal(self, list_1, list_2, n, rlist):  # list_1Q的位置, list_2：被解析的列表:
        x, y = list_1
        if list_2 != [] and list_2:
            for h in list_2[:-1]:  # 判断横坐标x在Y轴上方向上是否有Q（除本身对比的那行）
                if h[x] == 'Q':
                    return False
            value_1 = x - y
            value_2 = x + y
            for i in range(len(list_2) - 1):  # 判断向左上方向上是否有Q
                if i == y:
                    break
                if value_1 < 0:
                    value_1 += 1
                    continue
                else:
                    if list_2[i][value_1] == 'Q':
                        return False
                    value_1 += 1
            for o in range(len(list_2) - 1):  # 判断右上方向上是否有Q
                if o == y:
                    break
                if value_2 > n - 1:
                    value_2 -= 1
                    continue
                else:
                    if list_2[o][value_2] == 'Q':
                        return False
                    value_2 -= 1

        return True