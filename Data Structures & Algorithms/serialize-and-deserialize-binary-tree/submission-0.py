# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res=list()
        def dfs(node: Optional[TreeNode]):
            if node is None: 
                res.append('N')
                return
            else: res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print(res)
        return ','.join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print('data:',data)
        dataSrc=data.split(',')
        self.i=0
        def dfs():
            if dataSrc[self.i] == 'N':
                self.i+=1
                return None
            node = TreeNode(int(dataSrc[self.i]))
            self.i+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()
