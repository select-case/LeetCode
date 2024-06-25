# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lst_p = []
        head = root
        while head.val != p.val:
            lst_p.append(head.val)
            if head.val > p.val:
                head = head.left
            else: head = head.right
        lst_p.append(head.val)
        # print(lst_p)

        lst_q = []
        head = root
        while head.val != q.val:
            lst_q.append(head.val)
            if head.val > q.val:
                head = head.left
            else: head = head.right
        lst_q.append(head.val)
        # print(lst_q)

        short = len(lst_p) if len(lst_p) < len(lst_q) else len(lst_q)
        # print(short)
        ans = -1
        for i in range(short):
            if lst_p[i] == lst_q[i]:
                pass
            else:
                ans = lst_p[i-1]
                break
        if ans == -1:
            ans = lst_p[short-1]
        print(ans)
        head = root
        while head != None:

            if head.val == ans:
                return head
            elif head.val > ans:
                head = head.left
            else: head = head.right

