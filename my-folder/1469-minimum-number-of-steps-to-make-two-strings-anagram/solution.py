class Solution:
    def minSteps(self, s: str, t: str) -> int:
        letters = defaultdict(lambda: 0)
        for i in s:
            letters[i] += 1
        count = 0
        for i in t:
            if i in letters:
                letters[i] -= 1
            else: count += 1
        for i in letters:
            if letters[i] < 0:
                count += abs(letters[i])
    
        return count
