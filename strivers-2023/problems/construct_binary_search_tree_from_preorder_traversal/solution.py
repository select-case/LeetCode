# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0: return None
        root = TreeNode(nums[0])
        split = 1
        for i in range(1,len(nums)):
            if nums[i] < nums[0]:
                split += 1
        root.left = self.bstFromPreorder(nums[1:split])
        root.right = self.bstFromPreorder(nums[split:])
        return root