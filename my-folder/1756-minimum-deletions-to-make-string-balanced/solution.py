class Solution:
    def minimumDeletions(self, s: str) -> int:
        bc = 0
        min_deletions = 0
        for i in s:
            if i == 'a':
                min_deletions = min(min_deletions + 1, bc)
            else:
                bc += 1
        return min_deletions

