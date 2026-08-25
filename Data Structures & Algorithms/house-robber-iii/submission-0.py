# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:


        '''

        
        dfs ( take, dont ta)

        take -> ma

        withRoot = root + root.left.without + root.right.without
        wihoutRoot = root.left.with + root.right.with
        '''
        res = [0]
        def dfs(node):
            if not node:
                return (0,0)
            print(node.val)
            leftLower = dfs(node.left)
            rightLower = dfs(node.right)
           

            withNode = node.val + leftLower[1] + rightLower[1]
            withoutNode = max(leftLower[0], leftLower[1]) + max(rightLower[0], rightLower[1])

            print(res)
            res[0] = max(res[0], withNode, withoutNode)

            return (withNode, withoutNode)

        dfs(root)

        return res[0]

        