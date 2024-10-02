class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique_numbers = sorted(list(set(arr)))
        rank_dict = {}

        for idx in range(len(sorted_unique_numbers)):
            rank_dict[sorted_unique_numbers[idx]] = idx + 1
        
        for idx in range(len(arr)): 
            arr[idx] = rank_dict[arr[idx]]
        
        return arr

