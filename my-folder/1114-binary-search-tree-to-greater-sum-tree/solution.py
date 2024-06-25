# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        run_sum = 0
        def traversal(root):
            nonlocal run_sum
            if root.right:
                traversal(root.right)
            to_add = run_sum
            run_sum += root.val
            root.val = run_sum
            print(root.val)
            if root.left:
                traversal(root.left)
        traversal(root)
        return root
        
