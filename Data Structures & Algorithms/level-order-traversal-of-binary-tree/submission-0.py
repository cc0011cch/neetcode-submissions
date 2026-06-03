# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return list()
        queue = deque([(root, 1)])
        rst=list()
        l_lst=list()
        stage =0
        while queue:
            node, currentDepth= queue.popleft()
            if stage != currentDepth:
                if len(l_lst): rst.append(l_lst)
                l_lst= [node.val]
                stage+=1
            else:
                l_lst.append(node.val)
            if node.left: queue.append([node.left, currentDepth+1])
            if node.right: queue.append([node.right, currentDepth+1])
        rst.append(l_lst)
        return rst