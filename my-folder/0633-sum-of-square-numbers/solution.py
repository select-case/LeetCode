class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        num1 = 0
        num2 = int(sqrt(c))
        while num1 <= num2:
            if num1**2 + num2**2 == c: return True
            elif num1**2 + num2**2 > c: num2 -= 1
            else: num1 += 1
        return False
