class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        num2=[]
        num3=[]
        for i in nums:
            if i<0:
                num2.append(i)
            else:
                num3.append(i)
        num2.reverse()
        for i in range(len(num3)): num3[i]*=num3[i]
        for i in range(len(num2)): num2[i]*=num2[i]
        lst = []
        i=0
        j=0
        k=0
        while i<len(num3) and j < len(num2):
            if num3[i] <= num2[j]:
                lst.append(num3[i])
                i+=1
            else:
                lst.append(num2[j])
                j+=1
        while i<len(num3):
            lst.append(num3[i])
            i+=1
        while j<len(num2):
            lst.append(num2[j])
            j+=1
        return lst
