class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] in s[:i] + s[i+1:]:
                continue
            else:
                return i
        return -1
