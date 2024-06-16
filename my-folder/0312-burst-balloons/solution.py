class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l,r):
            if l > r:
                return 0
            elif (l,r) in dp:
                return dp[(l,r)]
            dp[(l,r)] = 0
            for i in range(l,r+1):
                coin = nums[l-1]*nums[i]*nums[r+1] + dfs(l,i-1) + dfs(i+1,r)
                dp[(l,r)] = max(dp[(l,r)],coin)
            return dp[(l,r)]
        return dfs(1,len(nums)-2)

# 1,3,1,5,8,1

# for i in range(1,4):
#     l = 1 r = 4
#     i = 1: coin = 1*3*1 + 0 + dfs(2,4)
#     i = 2: coin = 3*1*5 + 0 + dfs(3,4)
#     i = 3: coin = 1*5*8 + dfs(1,2) + 0

#     dfs[1,0] = 0
#     dfs(1,1) = 0
#     dfs(4,4) = 0

# fo
