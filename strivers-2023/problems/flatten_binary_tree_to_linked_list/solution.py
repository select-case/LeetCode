# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        def traversal(root):
            if root is None: return
            stack.append(root)
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        for i in range(len(stack)): 
            stack[i].left = None
            stack[i].right = None
        for i in range(len(stack)-1):
            stack[i].right = stack[i+1]