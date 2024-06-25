# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        lst = []
        def traversal(root):
            if root == None: return
            traversal(root.left)
            lst.append(root.val)
            traversal(root.right)
        traversal(root)
        sum_ = 0
        for i in lst:
            if i >= low and i <= high:
                sum_ += i
        return sum_