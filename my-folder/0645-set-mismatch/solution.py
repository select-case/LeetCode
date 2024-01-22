class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hash_map = {}
        for i in range(1,len(nums)+1):
            hash_map[i] = 0 
        for i in nums:
            hash_map[i] += 1
        ans = []
        for i in hash_map:
            if hash_map[i] == 2:
                ans.append(i)
        for i in hash_map:
            if hash_map[i] == 0:
                ans.append(i)
        return ans
