class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        start_1 = [1]
        start_0 = [0]
        for i in range(1,len(derived)):
            if derived[i-1] == 1:
                last = start_1[-1]
                start_1.append(1-last)
                last = start_0[-1]
                start_0.append(1-last)
            else:
                last = start_1[-1]
                start_1.append(last)
                last = start_0[-1]
                start_0.append(last)
        
        
        
        derived_new_0 = []
        for i in range(len(start_0)-1):
            derived_new_0.append(start_0[i]^start_0[i+1])
        derived_new_0.append(start_0[0]^start_0[-1])
        
        
        derived_new_1 = []
        for i in range(len(start_1)-1):
            derived_new_1.append(start_1[i]^start_1[i+1])
        derived_new_1.append(start_1[0]^start_1[-1])

        
        print(start_0)
        print(start_1)

        flag = False
        for i in range(len(derived)):
            if derived[i] == derived_new_0[i]:
                continue
            else: flag = True
        if flag == False: return True
        flag = False
        for i in range(len(derived)):
            if derived[i] == derived_new_1[i]:
                continue
            else: flag = True
        if flag == False: return True
        return False