class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        sum_ = len(A)*(len(A)+1)/2
        has = {}
        for i in A:
            if i in has:
                has[i] += 1
            else: has[i] = 1
        for i in has:
            if has[i] == 2:
                B = i
        for i in A: sum_ -= i
        return [B,int(B+sum_)]
