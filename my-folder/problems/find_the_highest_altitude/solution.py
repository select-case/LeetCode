class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_ = cur = 0
        for i in gain:
            cur += i
            if cur >= max_:
                max_ = cur
        return max_