class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        prev = [1] * n
        for i in range(k):
            cur = []
            sum_ = 0
            for i in prev:
                sum_ += i
                sum_ %= 1000000007
                cur.append(sum_)
            prev = cur
        print(cur)
        return cur[-1]%(1000000007)
