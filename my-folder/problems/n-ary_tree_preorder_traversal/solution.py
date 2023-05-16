"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        queue = [root]
        lst = []
        while queue != []:
            curr_node = queue.pop(-1)
            if curr_node != None:
                curr_node.children.reverse()
                for i in curr_node.children:
                    queue.append(i)
                lst.append(curr_node.val)
        return lst
    