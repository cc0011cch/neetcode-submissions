# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
# recursive:
#       return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1        
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        return max(left,right)+1
# iterative dfs.. but implementation of bfs is same.
#        stack=[(root,1)]
#        maxDepth=0

#        while(stack):
#            node, current_depth = stack.pop()
#            maxDepth=max(maxDepth,current_depth)

#            if node.left: 
#                stack.append((node.left, current_depth+1))
#            if node.right: 
#                stack.append((node.right,current_depth+1))
#        return maxDepth