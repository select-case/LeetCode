from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = permutations(nums)
        perm = list(perm)
        for i in range(len(perm)):
            perm[i] = list(perm[i])
        return perm