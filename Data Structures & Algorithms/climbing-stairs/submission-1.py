class Solution:
    def climbStairs(self, n: int) -> int:


        res = 0
        def dfs(i):
            nonlocal res

            if i == n:
                res += 1
                return
            if i > n:
                return

            dfs(i+1)
            dfs(i+2)
        dfs(0)
        return res

            




        