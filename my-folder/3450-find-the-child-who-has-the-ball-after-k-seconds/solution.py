class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        total = 2*n - 2
        req = k % total
        if req < n: return req
        req -= n
        req += 1
        while req:
            n -= 1
            req -= 1
        return n-1
        
