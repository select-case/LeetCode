class Solution:
    def isHappy(self, n: int) -> bool:
        visited = []
        while n>3:
            visited.append(n)
            temp = n
            A = []
            while temp>9:
                A.append(temp%10)
                temp = temp//10
            A.append(temp)
            n = 0
            for i in A:
                n += i*i
            if n in visited: 
                break
        return n==1