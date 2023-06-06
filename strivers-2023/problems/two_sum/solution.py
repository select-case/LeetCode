class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for p in range(len(nums)):
            current_number = nums_map.get(nums[p],-1)
            if current_number >= 0:
                return [current_number, p]
            else:
                matched_number = target - nums[p]
                nums_map[matched_number] = p
