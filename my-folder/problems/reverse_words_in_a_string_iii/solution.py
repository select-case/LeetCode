class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split(' ')
        temp = []
        for i in s:
            temp.append(i[::-1])
        ans = ""
        for i in range(len(temp)):
            ans+=temp[i]
            if i != len(temp)-1:
                ans+=" "
        return ans