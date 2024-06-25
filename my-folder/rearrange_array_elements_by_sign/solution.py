class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        lst_positive = []
        lst_negative = []
        for i in nums:
            if i>=0: lst_positive.append(i)
            else: lst_negative.append(i)
        for i in range(len(nums)):
            if i%2 == 0: nums[i] = lst_positive[i//2]
            else: nums[i] = lst_negative[i//2]
        return nums