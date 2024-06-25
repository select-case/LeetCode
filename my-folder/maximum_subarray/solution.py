class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        max_ = nums[0]
        for i in nums:
            cur += i
            if cur > max_:max_ = cur
            if cur < 0: cur = 0
        return max_