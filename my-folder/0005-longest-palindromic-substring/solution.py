class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        ans_str = s[0]
        for base in range(len(s)):
            left = 0
            right = 0
            while (base - left >= 0 and base + right < len(s)):
                # print(ans_str,base,left,right)
                if s[base - left] == s[base + right]:
                    if 2*left + 1 > max_len:
                        max_len = 2*left + 1
                        ans_str = s[base - left:base + right + 1]
                    left += 1
                    right += 1
                else:
                    break
        for base in range(0,len(s)-1):
            left = 0
            right = 0
            if s[base] == s[base + 1]:
                # print(ans_str,left,right)
                while (base - left >= 0 and base + 1 + right < len(s)):
                    if s[base - left] == s[base + right + 1]:
                        if max_len < 2*left + 2:
                            max_len = 2*left + 2
                            ans_str = s[base - left:base + right + 2]
                        left += 1
                        right += 1
                    else:
                        break
                        
            
            
            
        # print(max_len)
        # print(ans_str)
        return ans_str
