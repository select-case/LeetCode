class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs = sorted(strs)
        a = strs[0]
        b = strs[-1]
        print(strs)
        for i in range(min(len(a),len(b))):
            if(a[i]!=b[i]):
                return ans
            ans+=a[i]
        return ans