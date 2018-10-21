class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        def repeated(x):
            list_1 = []
            for i in x:
                if i in list_1:
                    return False
                if i in rlist:
                    list_1.append(i)
            return True

        for x in board:
            if not repeated(x):
                return False

        for x in range(9):
            list_2 = []
            for y in range(9):
                list_2.append(board[y][x])
            if not repeated(list_2):
                return False

        for m in range(3):
            for n in range(3):
                list_3 = []
                for x in range(3):
                    for y in range(3):
                        list_3.append(board[y + 3*n][x + 3*m])
                if not repeated(list_3):
                    return False

        return True

