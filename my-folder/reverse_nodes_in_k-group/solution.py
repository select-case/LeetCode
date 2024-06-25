# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        new = ListNode()
        new2 = new1 = new
        root = head
        while root:
            stack.insert(0,root.val)
            root = root.next
        
        while len(stack) >= k:
            curr = stack[-k:]
            stack = stack[:-k]
            for i in curr:
                new.val = i
                new.next = ListNode()
                new = new.next

        if len(stack) == 0:
            while new2:
                if new2.next.next == None:
                    new2.next = None
                new2 = new2.next

        for i in range(len(stack)-1,-1,-1):
            if i == 0:
                new.val = stack[i]
            else:
                new.val = stack[i]
                new.next = ListNode()
                new = new.next
        return new1