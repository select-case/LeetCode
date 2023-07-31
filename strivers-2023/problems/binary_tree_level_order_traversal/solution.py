# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     queue = [root]
    #     lst = []
    #     while queue != []:
    #         curr_node = queue.pop(0)
    #         if curr_node != None:
    #             if curr_node.left != None:
    #                 queue.append(curr_node.left)
    #             if curr_node.right != None:
    #                 queue.append(curr_node.right)
    #             lst.append(curr_node.val)
    #     print(lst)
    #     return [lst]
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        return ans