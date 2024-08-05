class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        a = defaultdict(int)
        for i in arr:
            a[i] += 1
        b = 0
        for i in a:
            if a[i] == 1:
                b += 1
            if b == k:
                return i
        return "" 
