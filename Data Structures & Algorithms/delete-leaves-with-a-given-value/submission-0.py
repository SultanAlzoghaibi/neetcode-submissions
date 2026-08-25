# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        '''

            if not node:
                return

            

            is leaf(right/left == null or keep(FALSE)) and target:
                return Remove
            remove the keep(FALSE)

            return keep(TRUE)
            


        '''

        def dfs(node):
            
            if not node:
                return False
            print(node.val)
           
            keepRight = dfs(node.right)
            keepLeft = dfs(node.left)

            
            if keepRight == False and keepLeft == False and node.val == target:
                return False

            if keepRight == False:
                node.right = None

            if keepLeft == False:
                node.left = None

            return True


        if root.val == target:
            return None

        dfs(root)
      
        return root

