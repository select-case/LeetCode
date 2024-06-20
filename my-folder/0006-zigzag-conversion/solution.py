class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        rows = [""] * numRows
        idx = 0
        inc = 1
        for i in s:
            rows[idx] += i
            if idx == 0:
                inc = 1
            elif idx == numRows - 1:
                inc = -1
            idx += inc
        return "".join(rows)
