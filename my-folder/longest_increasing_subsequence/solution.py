class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] =  max(dp[i],dp[j]+1)
        print(dp)
        return max(dp)
        # res = []
        # for x in nums:
        #     p = bisect_left(res, x)
        #     print(p,res,x)
        #     if p >= len(res):
        #         res.append(x)
        #     else:
        #         res[p] = x
        # print(res)
        # return len(res)