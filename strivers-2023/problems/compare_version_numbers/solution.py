class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1 = version1.strip().split('.')
        lst2 = version2.strip().split('.')
        for i in range(len(lst1)):
            lst1[i] = int(lst1[i])
        for i in range(len(lst2)):
            lst2[i] = int(lst2[i])
        print(lst1,lst2)
        for i in range(min(len(lst1),len(lst2))):
            if lst1[i] > lst2[i]: return 1
            if lst1[i] < lst2[i]: return -1
        if len(lst1) > len(lst2):
            for i in range(len(lst2),len(lst1)):
                if lst1[i] > 0: return 1
        if len(lst1) < len(lst2):
            for i in range(len(lst1),len(lst2)):
                if lst2[i] > 0: return -1
        return 0
