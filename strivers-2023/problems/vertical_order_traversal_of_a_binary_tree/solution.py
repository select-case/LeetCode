# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def traversal(head):
            if head == None: return
            head.val = [head.val,None,None]
            traversal(head.left)
            traversal(head.right)
        
        def assignvertical(head,level):
            if head == None: return
            head.val[1] = level
            assignvertical(head.left,level+1)
            assignvertical(head.right,level+1)

        def assignhorizontal(head,level):
            if head == None: return
            head.val[2] = level
            if level in ans:
                ans[level].append(head.val)
            else:
                ans[level] = [head.val]
            assignhorizontal(head.left,level-1)
            assignhorizontal(head.right,level+1)

        def traversal1(head):
            if head == None: 
                print(None)
                return
            print(head.val)
            traversal1(head.left)
            traversal1(head.right)

        ans = {}
        traversal(root)
        assignhorizontal(root,0)
        assignvertical(root,0)
        # traversal1(root)
        keys = ans.keys()
        keys = list(keys)
        keys.sort()
        final = []
        for key in keys:
            sorted_lst = sorted(ans[key], key=lambda x:(x[1],x[0]))
            ans[key] = sorted_lst
            lst = []
            for i in ans[key]:
                lst.append(i[0])
            final.append(lst)
        print(final)
        return final



        