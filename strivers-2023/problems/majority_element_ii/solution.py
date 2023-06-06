class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        has_ = {}
        for i in nums:
            if i in has_: has_[i] += 1
            else: has_[i] = 1
        ans = []
        for i in has_:
            if has_[i] > len(nums)//3:
                ans.append(i)
        return ans