class Solution:
    def climbStairs(self, n: int) -> int:

        res = 0


        def dfs(total):
            nonlocal res

            if total == n:
                res += 1
            
            if total > n:
                return

            dfs(total + 1)
            dfs(total + 2)
        
        dfs(0)

        return res






        