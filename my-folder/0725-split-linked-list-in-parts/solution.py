# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        idx = 0
        root = head
        while root:
            idx += 1
            root = root.next
        size, extra = idx//k, idx%k
        
        root = head
        result = []
        for i in range(k):
            part = root
            for j in range(size - 1 + (i < extra)):
                if root:
                    root = root.next
            if root:
                next_node = root.next
                root.next = None
                root = next_node
            result.append(part)
        
        return result

