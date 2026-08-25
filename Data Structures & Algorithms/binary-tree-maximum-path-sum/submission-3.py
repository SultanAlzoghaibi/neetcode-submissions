# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''

        return (including )
        '''

        res = [root.val]

        def dfs(node):

            if not node:
                return 0

            rightMax = dfs(node.right)
            leftMax = dfs(node.left)

            val = node.val + max(0, rightMax) + max(0, leftMax)
            res[0] = max(res[0], val)

            return node.val + max(0, rightMax, leftMax)


        dfs(root)
        return res[0]
        