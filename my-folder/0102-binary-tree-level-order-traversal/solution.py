# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal_lst = []
        def traversal(root,level):
            if root.left:
                traversal(root.left,level+1)
            traversal_lst.append([level,root.val])
            if root.right:
                traversal(root.right,level+1)
        if root is None: return []
        traversal(root,0)
        max_level = 0
        for entry in traversal_lst:
            if entry[0] > max_level:
                max_level = entry[0]
        ans_lst = []
        for i in range(max_level+1):
            ans_lst.append([])
        for i in traversal_lst:
            ans_lst[i[0]].append(i[1])
        return ans_lst
        
