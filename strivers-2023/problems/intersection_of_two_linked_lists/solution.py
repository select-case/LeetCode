# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dict_A = {}
        root = headA
        while root:
            dict_A[root] = root.next
            root = root.next
        root  =  headB
        while root:
            if root in dict_A:
                return root
            root = root.next
        return None