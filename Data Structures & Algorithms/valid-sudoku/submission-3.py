class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                current = board[r][c]
                if current in rows[r] or current in columns[c] or current in squares[r//3, c//3]:
                    return False
                if current != ".":
                    rows[r].add(current)
                    columns[c].add(current)
                    squares[r//3, c//3].add(current)
        return True