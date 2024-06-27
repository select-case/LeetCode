class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opens = 0
        close = 0
        ans_lst = []
        start = 0
        for i in range(len(s)):
            if s[i] == '(': opens += 1
            else: close += 1
            if opens == close:
                ans_lst.append(s[start:i+1])
                start = i+1
        ans_str = ""
        for i in ans_lst:
            ans_str += i[1:-1]
        return ans_str
