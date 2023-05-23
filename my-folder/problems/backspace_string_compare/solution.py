class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = ''
        for i in s:
            if i != '#':
                s1 += i
            else: s1 = s1[:-1]
        print(s1)

        s2 = ''
        for i in t:
            if i != '#':
                s2 += i
            else: s2 = s2[:-1]
        print(s2)
        
        return s1 == s2