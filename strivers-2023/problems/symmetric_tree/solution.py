# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None: return True
        def sym(left,right):
            if left is None and right is None:return True
            if left is None or right is None:return False
            return left.val == right.val and sym(left.left,right.right) and sym(left.right,right.left)
        return sym(root.right,root.left)
