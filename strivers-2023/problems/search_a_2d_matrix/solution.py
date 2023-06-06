class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        r = None
        for i in range(row):
            if matrix[i][0] == target: return True
            elif matrix[i][0] > target:
                r = i-1
                break
        if r == None: r = row - 1
        for j in range(col):
            if matrix[r][j] == target:
                return True
        return False