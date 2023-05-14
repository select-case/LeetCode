class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        lst = []
        dict_rec = {}
        for i in range(1,n+1):
            dict_rec[i] = 0
        initial = 1
        move_num = 1
        while dict_rec[initial] == 0: 
            print(initial)
            dict_rec[initial] = 1
            initial += move_num*k
            move_num += 1
            if initial%n == 0:
                initial = n
            else: initial = initial%n
        for i in dict_rec.keys():
            if dict_rec[i] == 0:
                lst.append(i)
        return lst