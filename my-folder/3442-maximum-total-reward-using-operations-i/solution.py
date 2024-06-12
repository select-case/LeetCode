class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        set1 = set()
        for i in rewardValues:
            dp = set1.copy()
            for j in set1:
                if j < i:
                    dp.add(j+i)
            dp.add(i)
            set1 = dp
        return max(set1)
            
