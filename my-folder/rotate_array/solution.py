class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return nums
        
        k = k % len(nums)
        lenght = len(nums)
        
        nums[lenght-k:], nums[:lenght-k] = nums[:lenght-k],nums[lenght-k:]