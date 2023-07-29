# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
            maxWidth = 0
            q = deque([(root, 1)])

            while q:
                maxWidth = max(maxWidth, q[-1][1] - q[0][1] + 1)
                for _ in range(len(q)):
                    n, i = q.popleft()
                    if n.left: q.append((n.left, i * 2))
                    if n.right: q.append((n.right, i * 2 + 1))
            return maxWidth