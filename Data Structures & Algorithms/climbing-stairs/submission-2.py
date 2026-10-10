class Solution:
    def climbStairs(self, n: int) -> int:
        

        '''

        0 + 2
        1 + 1

        
        '''
        res =0

        cache = {} #number: combinationCnt

        def dfs(currVal):
            nonlocal res

            if currVal == n:
                res += 1
                return 1
            
            if currVal >= n:
                return 0
            
            if currVal in cache:
                return cache[currVal]


            
            jump1 = dfs(currVal+1)
            jump2 = dfs(currVal+2)

            cache[currVal] = jump1 + jump2

            return jump1 + jump2

        return dfs(0)

        