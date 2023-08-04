# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q or root == None: return root
        x = self.lowestCommonAncestor(root.left,p,q)
        y = self.lowestCommonAncestor(root.right,p,q)
        if x == None: return y
        elif y == None: return x
        else: return root
