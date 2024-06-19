class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if m * k > n: return -1

        def fun(d):
            l,b = 0,0

            i = 0
            while i<n:
                while i<n and bloomDay[i]<=d:
                    l+=1
                    if l==k:
                        b+=1
                        l=0
                    i+=1
                if i<n and bloomDay[i]>d: l=0
                if b>m: return True
                i+=1
            return b>=m

        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = l + (r - l) // 2
            if fun(mid):
                r = mid
            else:
                l = mid + 1
        return l


