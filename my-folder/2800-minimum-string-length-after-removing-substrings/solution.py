class Solution:
    def minLength(self, s: str) -> int:
        lst = []
        for i in s:
            lst.append(i)
            if len(lst) >= 2:
                s1 = lst[-2] + lst[-1]
                if s1 == "AB" or s1 == "CD":
                    lst = lst[:-2]
        return len(lst)
