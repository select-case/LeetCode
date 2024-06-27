class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        mismatches = 0
        lst = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                mismatches += 1
                lst.append((i,s[i],goal[i]))
        # if mismatches != 0 or mismatches != 2: return False
        if mismatches == 2:
            if lst[0][1] == lst[1][2] and lst[0][2] == lst[1][1]: return True
            return False
        if mismatches == 0:
            counter = defaultdict(lambda:0)
            for i in s:
                counter[i] += 1
            for i in counter:
                if counter[i] >= 2:
                    return True
        return False
        
        
