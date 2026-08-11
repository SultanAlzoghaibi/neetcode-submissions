# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        '''
        DFS
        (node, maxVal)
        if node > maxVal:
            res += 1

        '''
        
        res = [1]

        def dfs(node, maxVal):
            
            if not node:
                return
            #print(node.val, maxVal)

            if node.val >= maxVal:
                maxVal = node.val
                res[0] += 1
            
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)


        dfs(root, root.val)

        return res[0] - 1