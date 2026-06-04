# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validation(node: Optional[TreeNode], left:int, right:int) -> bool:
            if node is None: return True
            if not(node.val < right and node.val >left): return False
            return validation(node.left, left, node.val) and validation(node.right,node.val,right)

        return validation(root, float('-inf'),float('inf'))


        