class Solution:
    def partitionString(self, s: str) -> int:
        set1 = set()
        count = 0
        for i in s:
            n = len(set1)
            set1.add(i)
            if n == len(set1):
                count += 1
                print(set1)
                set1 = set()
                set1.add(i)
            else:
                pass
        return count + 1

        
