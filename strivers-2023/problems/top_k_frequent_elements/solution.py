class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        ans =  [i[0] for i in cnt.most_common(k)]
        return ans