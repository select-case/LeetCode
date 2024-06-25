class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        cost = [0] * (n+1)
        cost[0] = nums[0]
        cost[1] = max(nums[0],nums[1])
        for i in range(2,n):
            cost[i] = max(cost[i-2]+nums[i],cost[i-1])
        print(cost)
        return cost[n-1]