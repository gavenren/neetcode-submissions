class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(9):
            compare = []
            for i in range(9):
                if board[x][i] != ".":
                    if board[x][i] in compare:
                        return False
                    compare.append(board[x][i])
        for x in range(9):
            compare = []
            for i in range(9):
                if board[i][x] != ".":
                    if board[i][x] in compare:
                        return False
                    compare.append(board[i][x])
        for z in range(0, 8, 3):
            for y in range(0, 8, 3):
                compare = []
                for x in range(3):
                    for i in range(3):
                        if board[y+i][z+x] != ".":
                            if board[y+i][z+x] in compare:
                                return False
                            compare.append(board[y+i][z+x])
        return True