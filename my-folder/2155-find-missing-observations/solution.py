class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        expected_sum = mean * (len(rolls) + n)
        remaining = expected_sum - sum(rolls)
        if remaining > 6*n or remaining < n: return []

        ans = [1] * n
        remaining -= n
        idx = 0
        while remaining > 5:
            ans[idx] += 5
            remaining -= 5
            idx += 1
        ans[idx] += remaining

        return ans
