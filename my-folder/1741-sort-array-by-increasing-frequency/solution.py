class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        map_ = {}
        for i in nums:
            if i in map_:
                map_[i] += 1
            else:
                map_[i] = 1
        lst = [(map_[i],i) for i in map_]
        lst.sort(key = lambda x:(x[0],-x[1]))
        lst1 = []
        for i in lst:
            for j in range(i[0]):
                lst1.append(i[1])
        print(lst1)
        return lst1
