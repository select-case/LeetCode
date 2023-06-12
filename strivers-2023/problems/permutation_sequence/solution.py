class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        lst = [i for i in range(1,n+1)]
        s = ''
        f = n-1
        k -= 1
        for i in range(n):
            ans = k//math.factorial(f)
            k %= math.factorial(f)
            s += str(lst[ans])
            lst.pop(ans)
            f -= 1
        print(s)
        return s