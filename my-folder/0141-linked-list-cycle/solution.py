# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        if slow is None or slow.next is None or slow.next.next is None: return False
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: return True
        return False
        
