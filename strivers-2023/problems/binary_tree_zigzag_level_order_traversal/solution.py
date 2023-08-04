# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def bfs(curr = root, level = 0):
            nonlocal ans
            if curr:
                if len(ans) > level:
                    ans[level].append(curr.val)
                else:
                    ans.append([curr.val])
                bfs(curr.left, level + 1)
                bfs(curr.right, level + 1)
            return
        bfs()
        for i in range(len(ans)):
            if i % 2 == 1:
                ans[i].reverse()


        return ans