class Solution:
    # def maxProduct(self, nums: List[int]) -> int:
    #     dp = nums.copy()
    #     for i in range(len(nums)):
    #         for j in range(i):
    #             dp[i] = max(dp[j]*nums[i],dp[i])
    #     return max(dp)
    def maxProduct(self, nums: List[int]) -> int:
        maxi = -10000000
        prod = 1
        for i in nums:
            prod *= i
            maxi = max(prod,maxi)
            if prod == 0: prod = 1
        prod = 1
        nums.reverse()
        for i in nums:
            prod *= i
            maxi = max(prod,maxi)
            if prod == 0: prod = 1
        return maxi
