class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_right = 0
        sum_left = 0
        for i in nums:
            sum_right += i
        sum_right -= nums[0]
        if sum_right == sum_left:
            return 0
        for i in range(1,len(nums)):
            sum_right -= nums[i]
            sum_left += nums[i-1]
            if sum_right == sum_left:
                return i
         
        return -1