import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10001
        profit = 0
        for i in range(len(prices)):
            min_price = min(min_price,prices[i])
            profit = max(profit,prices[i] - min_price)
        return profit