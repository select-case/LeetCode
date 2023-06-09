# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        print(stack)
        while len(stack) > 1:
            a = stack[0]
            b = stack[-1]
            if a != b: return False
            stack = stack[1:-1]
        return True 

# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         fast = head
#         slow = head

#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#         prev = None
#         while slow:
#             tmp = slow.next
#             slow.next = prev
#             prev = slow
#             slow = tmp
        
#         left, right = head, prev
#         while right:
#             if left.val != right.val:
#                 return False
#             left = left.next
#             right = right.next
#         return True