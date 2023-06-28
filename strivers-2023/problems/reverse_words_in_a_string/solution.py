class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        ans = ''
        for i in s:
            ans += i
            ans += ' '
        return ans[:-1]