class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        if len(s) <= 2:
            if int(s) == 20: return 1
            if int(s) <= 26 and int(s) >= 11: return 2
            # elif int(s) == 0: return 0
            elif int(s) >= 30 and int(s)%10 == 0: return 0
            else: return 1
        
        
        
        
        dp = [0] * (len(s) + 1)
        if s[-1] == '0': pass
        else: 
            dp[-2] = 1
        dp[-1] = 1
        # print(dp)

        idx = len(s) - 2
        while idx >=0:
            if int(s[idx]) == 0: dp[idx] = 0
            elif int(s[idx:idx+2]) <= 26 and int(s[idx:idx+2]) >= 10:
                dp[idx] = dp[idx+1] + dp[idx+2]
            else:
                dp[idx] = dp[idx+1]
            idx -= 1
        print(dp)
        return dp[0]