class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total_count = 0
        dp = [defaultdict(int) for _ in range(len(nums))]

        print(dp)

        for i in range(1,len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    total_count += dp[j][diff]
        print(dp)
        return total_count