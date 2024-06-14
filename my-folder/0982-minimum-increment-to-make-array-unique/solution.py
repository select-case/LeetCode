class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        track = 0
        inc = 0
        for num in nums:
            track = max(num,track)
            inc += track - num
            track += 1
        return inc
