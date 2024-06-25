class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # cur_ = 100000
        min_ = 100000
        for i in range(len(nums)-1):
            first = nums[i]
            start = i + 1
            end = len(nums)-1
            while start < end:
                sum_ = first + nums[start] + nums[end]
                if target == sum_: return target
                if abs(target - sum_) < min_:
                    min_ = abs(target - sum_)
                    ans = sum_
                if sum_ > target:
                    end -= 1
                else:
                    start += 1
        return ans
