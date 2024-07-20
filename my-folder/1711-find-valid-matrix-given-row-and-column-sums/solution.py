class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row, col = 0, 0
        matrix  = [[0 for i in range(len(colSum))] for j in range(len(rowSum))]
        while row < len(rowSum) and col < len(colSum):
            matrix[row][col] = min(rowSum[row],colSum[col])
            term = min(rowSum[row],colSum[col])
            rowSum[row] -= term
            colSum[col] -= term
            if rowSum[row] == 0:
                row += 1
            if colSum[col] == 0:
                col += 1
        return matrix
