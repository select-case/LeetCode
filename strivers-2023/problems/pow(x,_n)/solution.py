class Solution:
    def myPow(self, x: float, n: int) -> float:
        # n_ = n
        # n = abs(n)
        # ans = 1
        # while(n != 0):
        #     if n%2 == 0:
        #         x *= x
        #         n /= 2
        #     else:
        #         n -= 1
        #         ans *= x
        # if n_ < 0:
        #     ans = 1/ans
        # return ans

        return x**n