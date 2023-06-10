"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        z = Node(0)
        dict_ = {}
        cur,copy = head,z
        while cur:
            copy.next = Node(cur.val)
            dict_[cur] = copy.next
            cur = cur.next
            copy = copy.next
        
        cur,copy = head,z.next
        while cur:
            copy.random = dict_[cur.random] if cur.random else None
            cur, copy = cur.next, copy.next
        
        return z.next 
        