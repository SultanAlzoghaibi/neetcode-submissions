# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        

        def dfs(root, maxN):
            nonlocal count

            if not root:
                return
            if root.val >= maxN:
                print(root.val)
                count += 1
                
            maxN = max(maxN, root.val)
            dfs(root.left, maxN)
            dfs(root.right, maxN)


        dfs(root,root.val)
        return count

        