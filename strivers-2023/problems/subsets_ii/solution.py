class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def helper(ind,ans1):
            ans.append(ans1)
            for i in range(ind, len(nums)):
                if i > ind and nums[i] == nums[i-1]:
                    continue
                helper(i+1, ans1+[nums[i]])
        helper(0, [])
        return ans