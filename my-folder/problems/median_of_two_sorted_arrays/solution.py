class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1 + nums2
        nums1 = sorted(nums1)
        if len(nums1) % 2 == 0:
            return (nums1[len(nums1)//2 - 1] + nums1[(len(nums1)//2)])/2 
        else:
            n = math.ceil(len(nums1)/2)
            return nums1[n-1]
