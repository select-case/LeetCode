class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        nums.sort()
        if not nums: return []
        a = nums[0]
        b = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                b = nums[i]
            else:
                if a == b:
                    ans.append(str(a))
                else:
                    ans.append(str(a)+"->"+str(b))
                a = nums[i]
                b = nums[i]
        if a == b:
            ans.append(str(a))
        else:
            ans.append(str(a)+"->"+str(b))
        return ans
