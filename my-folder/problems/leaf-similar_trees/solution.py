# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaf_traversal(root,lst):
            if not root:
                return
            if not root.left and not root.right:
                lst.append(root.val)
                print(lst)
                return lst
            leaf_traversal(root.left,lst)
            leaf_traversal(root.right,lst)
        lst1 = []
        lst2 = []
        leaf_traversal(root1,lst1)
        leaf_traversal(root2,lst2)
        print(lst1,lst2)
        return lst1 == lst2

        

