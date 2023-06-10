class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ = 0
        cur = 0
        for i in nums:
            if i == 1:
                cur += 1
                if cur > max_:
                    max_ = cur
            else:
                cur = 0
        return max_