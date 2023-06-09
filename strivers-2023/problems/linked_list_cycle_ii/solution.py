# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        new = head
        while True:
            if fast == None:
                return None
            elif fast.next == None:
                return None
            elif fast.next.next == None:
                return None
            else:
                fast = fast.next.next
                slow = slow.next
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
                # while True:
                #     if new == slow:
                #         return pos
                #     else:
                #         new = new.next
                #         pos += 1
