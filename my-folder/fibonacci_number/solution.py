class Solution:
    def fib(self, n: int) -> int:
        lst = [0,1]
        for i in range(n):
            lst.append(lst[-2]+lst[-1])
        return lst[-2]