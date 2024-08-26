"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def traversal(root):
            if root == None: return
            for child in root.children:
                traversal(child)
            # traversal(root.right)
            ans.append(root.val)
        traversal(root)
        return ans
