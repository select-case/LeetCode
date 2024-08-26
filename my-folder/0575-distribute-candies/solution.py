class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        map_ = {}
        for i in candyType:
            if i in map_:
                map_[i] += 1
            else:
                map_[i] = 1
        ans = list(map_.values())
        ans.sort()
        eatable = len(candyType)//2
        sum_ = 0
        if len(ans) >= eatable:
            return eatable
        else:
            return len(ans)
