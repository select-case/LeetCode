class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        nums.sort()
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        return nums
