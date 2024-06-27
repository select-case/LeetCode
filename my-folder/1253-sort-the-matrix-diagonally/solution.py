class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        ans = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        lists = {}
        for i in range(len(mat)):
            lists[(i,0)] = []
        for j in range(len(mat[0])):
            lists[(0,j)] = []
        for idx in lists:
            row = idx[0]
            col = idx[1]
            while row < len(mat) and col < len(mat[0]):
                lists[idx].append(mat[row][col])
                row += 1
                col += 1
        for i in lists:
            lists[i].sort()
        print(lists)
        for idx in lists:
            print(idx)
            row = idx[0]
            col = idx[1]
            entry = 0
            while row < len(mat) and col < len(mat[0]):
                print(row,col,entry)
                ans[row][col] = lists[idx][entry]
                row += 1
                col += 1
                entry += 1
        return ans
