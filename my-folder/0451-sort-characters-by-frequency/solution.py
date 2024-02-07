class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        lst = []
        for i in hashmap:
            lst.append([hashmap[i],i])
        lst.sort()
        print(lst)
        ans = ''
        for i in range(len(lst)-1,-1,-1):
            for j in range(lst[i][0]):
                ans += lst[i][1]
        return ans
