# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # fast = head
        # lst = []
        # while fast:
        #     lst.append(fast)
        #     fast = fast.next
        # ans = lst[0]
        # lst = lst[1:]
        # flag = 1
        # for i in range(len(lst)):
        #     lst[i].next = None
        # print(lst)
        # while len(lst) != 0:
        #     if flag == 1:
        #         ans.next = lst[-1]
        #         lst = lst[:-1]
        #         flag = 0
        #     else:
        #         ans.next = lst[0]
        #         lst = lst[1:]
        #         flag = 1
        #     ans = ans.next
        if not head: return
        slow,fast = head,head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        prev,curr = None,slow.next
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        slow.next = None
        
        head1, head2 = head, prev
        while head2:
            next_ = head1.next
            head1.next = head2
            head1 = head2
            head2 = next_




        