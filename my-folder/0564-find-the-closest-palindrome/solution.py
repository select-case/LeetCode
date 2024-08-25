import re
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        '''
        if n.len == 1: return n - 1
        if n.len == 2: return n - n%11 or n*(n//11 + 1)
        if n.len == 3: return match n first and last digit

        1234
        1221

        10
        1199 
        1221

        101

        '''
        if len(n) == 1:
            return str(int(n) - 1)

        x = re.search("^9{1,18}$",n)
        if x: return str(int(n) + 2)

        x = re.search("^10{0,18}1$",n)
        if x: return str(int(n) - 2)

        x = re.search("^10{0,18}$",n)
        if x: return str(int(n) - 1)

        if len(n)%2 == 0:
            mid = n[len(n)//2]

        if len(n)%2:
            int_n = int(n)
            part_1 = n[:len(n)//2]
            int_part_1 = int(part_1)
            mid =  int(n[len(n)//2])
            mid_str = str(mid)
            
            if mid > 0 and mid < 9:
                options = [str(int_part_1) + str(mid - 1), str(int_part_1)+str(mid), str(int_part_1)+ str(mid + 1)]
            elif mid == 0:
                options = [str(int_part_1) + str(mid), str(int_part_1) + str(mid + 1)]
            else:
                options = [str(int_part_1) + str(mid - 1), str(int_part_1) + str(mid)]

            for i in range(len(options)):
                options[i] = options[i] + part_1[::-1]
            mini = 10**18
            idx = None
            print(options)
            for i in range(len(options)):
                if abs(int_n - int(options[i])) < mini and abs(int_n - int(options[i])) != 0:
                    mini = abs(int_n - int(options[i]))
                    idx = i
                print(i, options[i], mini)
            return options[idx]

        
        
        else: 
            int_n = int(n)
            part_1 = n[:len(n)//2]
            int_part_1 = int(part_1)
            options = [str(int_part_1 - 1),str(int_part_1 ),str(int_part_1 + 1)]
            for i in range(len(options)):
                options[i] = options[i] + options[i][::-1]
            mini = 10**18
            idx = None
            for i in range(len(options)):
                if abs(int_n - int(options[i])) < mini and abs(int_n - int(options[i])) != 0:
                    mini = abs(int_n - int(options[i]))
                    idx = i
            return options[idx]


        return 0

