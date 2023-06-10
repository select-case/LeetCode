class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        for i in range(len(nums) - 2):
            first = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                second = nums[j]
                third = nums[k]
                potential = first + second + third
                if potential == 0: 
                    triplets.add((first,second,third))
                    j += 1
                    k -= 1
                elif potential > 0: k -= 1
                else: j += 1
        return triplets