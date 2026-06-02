# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:  return True

        self.T=True
        def SameTree( p: Optional[TreeNode], q: Optional[TreeNode]) :
            if p is None and q is None:
                self.T= self.T and True
                return 

            if p is None or q is None:  
                self.T= self.T and False
                return

            if p.val == q.val:  
                 self.T= self.T and True
                 SameTree(p.left,q.left)
                 SameTree(p.right,q.right)

                 return
            else: 
                self.T= self.T and False 
                return
        SameTree(p,q)


        return self.T
