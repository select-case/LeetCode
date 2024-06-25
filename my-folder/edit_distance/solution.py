class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if not m or not n: return max(m, n)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1):
            dp[m][j] = n - j
        for i in range(m + 1):
            dp[i][n] = m - i
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i][j+1],dp[i+1][j],dp[i+1][j+1]) + 1
        print(dp)
        return dp[0][0]



        print(dp)

        return 0
        