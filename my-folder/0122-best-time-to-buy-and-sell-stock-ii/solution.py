class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought = False
        buyprice = 0
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] > prices[i+1] and bought:
                print(i,"Sell")
                bought = False
                profit += prices[i] - buyprice
            if prices[i] < prices[i+1] and not bought:
                print(i,"Buy")
                bought = True
                buyprice = prices[i]

        if bought:
            profit += prices[-1] - buyprice
            print(len(prices)-1,"Sell")

        return profit
            
            
