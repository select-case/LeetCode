class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = b = 0
        for i in nums:
            if a == 0:
                b = i
            if b == i:
                a += 1
            else: a -= 1
        return b 