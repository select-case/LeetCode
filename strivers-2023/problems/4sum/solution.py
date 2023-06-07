class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruplets = set()
        for i in range(len(nums) - 3):
            first = nums[i]
            for j in range(i+1,len(nums)-2):
                second = nums[j]
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    third = nums[k]
                    fourth = nums[l]
                    potential = first + second + third + fourth
                    if potential == target: 
                        quadruplets.add((first,second,third,fourth))
                        k += 1
                        l -= 1
                    elif potential > target: l -= 1
                    else: k += 1
        return quadruplets
