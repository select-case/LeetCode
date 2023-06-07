class Solution:
    def maxLen(self,n, A):
        hash_ = {}
        maxidx = 0
        sum_ = 0
        for i in range(n):
            sum_ += A[i]
            if sum_ == 0:
                maxidx = i + 1
            else:
                if sum_ in hash_:
                    maxidx = max(maxidx, i - hash_[sum_])
                else:
                    hash_[sum_] = i
        return maxidx
