class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dict_ = {}
        for i in nums:
            if i in dict_: dict_[i] += 1
            else: dict_[i] = 1
        l = []
        while len(dict_.keys()) > 0:
            lst = []
            to_del = []
            for i in dict_:
                lst.append(i)
                dict_[i] -= 1
                if dict_[i] == 0:
                    to_del.append(i)
            for i in to_del:
                del dict_[i]
            l.append(lst)
        return l
