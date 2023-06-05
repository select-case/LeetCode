class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        has = {}
        for i in nums:
            if i in has:
                has[i] += 1
            else: has[i] = 1
        for i in has:
            if has[i] >= 2:
                return i