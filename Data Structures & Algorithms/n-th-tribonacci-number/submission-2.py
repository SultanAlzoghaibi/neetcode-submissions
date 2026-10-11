class Solution:
    def tribonacci(self, n: int) -> int:



        dp1 = 0
        dp2 = 1
        dp3 = 1
        earlyTribo = {0:0,1:1,2:1}
        for i in range(n-3):
            dp1, dp2, dp3 = dp2, dp3, (dp1 + dp2 + dp3)

        if n < 3:
            return earlyTribo[n]
        
        return (dp1 + dp2 + dp3)


        