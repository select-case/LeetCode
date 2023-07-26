from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict()
        for i in nums:
            if i not in d: d[i] = 1
            else: d[i] += 1
        for i in d:
            if d[i] > 1: return True
        return False