import bisect
class Solution:
    def search(self, nums, target):
        idx = bisect_right(nums, target)

        if idx > 0 and nums[idx - 1] == target:
            return idx - 1
        else:
            return -1