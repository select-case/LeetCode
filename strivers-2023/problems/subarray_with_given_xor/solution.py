from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A) 
        xr = 0
        map_ = defaultdict(int)
        map_[xr] = 1 
        count = 0

        for i in range(n):
            
            xr = xr ^ A[i]
            x = xr ^ B
            count += map_[x]
            map_[xr] += 1
        return count
