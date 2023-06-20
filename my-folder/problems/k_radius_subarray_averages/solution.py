class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n <= 2*k : return [-1] * n
        if k == 0: return nums 
        ans = [0] * n
        sum_ = 0
        for i in range(k):
            ans[i] = -1
            ans[-i-1] = -1
        for i in range(2*k+ 1):
            sum_ += nums[i]
        nums.append(0)
        for i in range(k,len(nums) - k - 1):
            ans[i] = sum_//(2*k+1)
            sum_ -= nums[i - k]
            sum_ += nums[i + k + 1]
        
        return ans