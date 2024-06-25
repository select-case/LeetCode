class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return None
        nums.sort()
        return nums[-k]