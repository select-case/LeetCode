class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x = stones.pop(-1)
            y = stones.pop(-1)
            stones.append(abs(x-y))
            if stones[-1] == 0: stones.pop(-1)
        if len(stones) == 0: return 0
        else: return stones[0]