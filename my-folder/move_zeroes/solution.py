class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        last_non_zero = 0
        cur = 0
        while(cur<n):
            if(nums[cur]!=0):
                nums[cur],nums[last_non_zero] = nums[last_non_zero],nums[cur]
                last_non_zero+=1
            cur+=1
                
