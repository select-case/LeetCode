import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        lst1 = []
        lst2 = []
        for i in range(1,int(math.sqrt(n))+1):
            if n % i == 0:
                if n/i == i:
                    lst1.append(i)
                else:
                    lst1.append(i)
                    lst2.insert(0,int(n/i))
        lst = lst1 + lst2
        print(lst)
        if k > len(lst): return -1
        else: return lst[k-1]