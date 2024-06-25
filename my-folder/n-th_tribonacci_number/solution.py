class Solution:
    def tribonacci(self, n: int) -> int:
        lst = [0,1,1]
        for i in range(n):
            lst.append(lst[-2]+lst[-1]+lst[-3])
        return lst[-3]