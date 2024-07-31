class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [float('inf')] * (len(books) + 1)
        dp[0] = 0
        for i in range(1,len(books) + 1):
            width = 0
            height = 0
            for j in range(i, 0, -1):
                width += books[j-1][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j-1][1])
                dp[i] = min(dp[i], dp[j-1] + height)
        
        return dp[-1]

