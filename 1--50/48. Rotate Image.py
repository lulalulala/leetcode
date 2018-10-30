"""Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        import copy
        n = len(matrix)
        if n == 0:
            return [[]]
        list_1 = copy.deepcopy(matrix)
        for i in range(n):
            for x in range(n):
                matrix[x][i] = list_1[n - i - 1][x]
