class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        sign = 1
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = 1 if s[i] == '+' else -1
            i += 1
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if res > (2**31 - 1) // 10 or (res == (2**31 - 1) // 10 and digit >= 8):
                return 2**31 - 1 if sign == 1 else -2**31
            res = res * 10 + digit
            i += 1
        return res*sign
