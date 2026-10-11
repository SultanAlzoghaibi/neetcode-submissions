class Solution:
    def climbStairs(self, n: int) -> int:
        

        '''

        0 + 2
        1 + 1

        
        '''
        dp1 = 1
        dp2 = 1

        for i in range(n-1):
            temp = dp1
            dp1 = dp1 + dp2
            dp2 = temp

        return dp1

        