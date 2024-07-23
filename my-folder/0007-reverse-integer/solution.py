class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31 - 1 or x < -(2**31):
            return 0
        x = str(x)
        flag = False
        if x[0] == '-':
            flag = True
            x = x[1:]
        x = x[::-1]
        x = int(x)
        if flag:
            x = x*-1
        if x > 2**31 - 1 or x < -(2**31):
            return 0
        return x
