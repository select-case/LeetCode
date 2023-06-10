class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        to = []
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                to.append(i)
        print(to)
        to.reverse()
        for i in to:
            nums.pop(i)
