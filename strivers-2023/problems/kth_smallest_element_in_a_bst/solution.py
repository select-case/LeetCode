# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def traversal(root):
            nonlocal ans
            if root is None: return
            traversal(root.left)
            ans.append(root.val)
            traversal(root.right)
        traversal(root)
        print(ans)
        return ans[k-1]