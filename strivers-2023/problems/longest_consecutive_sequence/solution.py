class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        hash_ = {}
        for i in nums:
            hash_[i] = 1
        # count = 0
        # count_max = 0
        # for i in hash_:
        #     while i+1 in hash_:
        #         count += 1
        #         i += 1
        #     if count > count_max: count_max = count
        #     count = 0
        # return count_max+1
        nums = list(hash_.keys())
        nums.sort()
        count = 0
        count_max = 0
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                count += 1
                if count > count_max: count_max = count
            else:
                count = 0
        return count_max+1

        