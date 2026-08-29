# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        code = []
        def dfs(node):
            if not node:
                code.append("N")
                return
            
            code.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(code)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",") 

        self.i = 0
        def dfs():
            
            if len(vals) <= self.i or vals[self.i] == "N" :
                self.i += 1
                return None
            
            
            
            val = int(vals[self.i])
            self.i += 1
            left = dfs()
            right = dfs()
            
            return TreeNode(val, left, right)

        return dfs()
                
