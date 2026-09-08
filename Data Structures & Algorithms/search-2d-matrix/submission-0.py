class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length = len(matrix[0])
        height = len(matrix)
        l = 0
        r = (length * height) - 1

        while l <= r:
            middle = (l + r) // 2
            row = middle // length
            column = middle % length
            if target == matrix[row][column]:
                return True
            elif target < matrix[row][column]:
                r = middle - 1
            else:
                l = middle + 1
        return False
