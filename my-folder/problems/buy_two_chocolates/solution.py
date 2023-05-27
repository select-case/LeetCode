class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        cheap1 = min(prices[0],prices[1])
        cheap2 = max(prices[0],prices[1])
        for i in range(2,len(prices)):
            if prices[i] <= cheap1:
                cheap2 = cheap1
                cheap1 = prices[i]
            elif prices[i] < cheap2:
                cheap2 = prices[i]
        print(cheap1,cheap2)
        if money - cheap1 - cheap2 >= 0: return money - cheap1 - cheap2
        else: return money

        