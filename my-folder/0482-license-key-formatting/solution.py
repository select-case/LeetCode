class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        print(s)
        lst = []
        for i in s:
            if i is not '-':
                lst.append(i)
        n = len(lst)
        base = ''.join(lst[:n%k])
        lst = lst[n%k:]
        for i in range(0,len(lst),k):
            base += "-"
            base += ''.join(lst[i:i+k])
        if len(base) > 0:
            if base[0] == '-':
                base = base[1:]
        return base
        
                
        
