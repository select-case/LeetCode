class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        lst = [0,1]
        for i in range(n):
            lst.append(lst[-1]+lst[-2])
        print(lst)
        return lst[-2]
