class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = float('inf')
        profit = 0
        for i in prices:
            price = min(price,i)
            profit = max(profit, i - price)
        return profit
