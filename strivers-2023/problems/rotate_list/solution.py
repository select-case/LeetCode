# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        count = 0
        root = head
        while root:
            count += 1
            root = root.next
        print(count)
        k %= count
        for i in range(k):
            root = head
            temp = root.val
            while root.next:
                temp2 = root.next.val
                root.next.val = temp
                temp = temp2
                root = root.next
            head.val = temp
        return head