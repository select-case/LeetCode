class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = [[1]]
        if numRows == 1: return lst
        lst.append([1,1])
        if numRows == 2: return lst
        for i in range(numRows-2):
            lst.append([1])
            for i in range(len(lst[-2])-1):
                lst[-1].append(lst[-2][i]+lst[-2][i+1])
            lst[-1].append(1)
        return lst