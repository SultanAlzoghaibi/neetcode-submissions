# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        parentMap = {}
        # Node: [parentNode1, parentNode2, ...]


        
        def dfs(node, parentList):
            
            nonlocal p
            nonlocal q 

            if not node:
                return

            if not parentList: 
                parentMap[node] = [node]
            else:
                parentMap[node] = parentList.copy()
                print(type(parentMap[node]))
                parentMap[node].append(node)


            dfs(node.right, parentMap[node])
            dfs(node.left, parentMap[node])

        dfs(root, None)
        print({k.val: [p.val if p else None for p in v] for k, v in parentMap.items()})        
        common = []

        if len(parentMap[q]) < len(parentMap[p]):
            evaluateNode = q
            biggerNodeList = p
        else:
            evaluateNode = p
            biggerNodeList = q

        for i in range(min( len(parentMap[q]) , len(parentMap[p]))):
            
            if parentMap[evaluateNode][i] in parentMap[biggerNodeList]:

                common.append(parentMap[evaluateNode][i])
        print("common")
        
        print([n.val for n in common])
        
        res = [0, None]

        for node in common:
            print(len(parentMap[node]), res)
            if len(parentMap[node]) > res[0]:
                res[1] = node
                res[0] = len(parentMap[node])

       
        return res[1]
        

        

