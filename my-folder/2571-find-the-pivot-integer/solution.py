class Solution:
    def pivotInteger(self, n: int) -> int:
        sum1 = n*(n+1)/2
        sum2 = n
        for i in range(n,-1,-1):
            if sum1 == sum2: return i 
            sum1 -= i
            sum2 += i - 1
        return -1


