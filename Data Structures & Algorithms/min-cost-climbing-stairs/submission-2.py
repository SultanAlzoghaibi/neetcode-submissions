class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        take the last value
        '''

        dp1 = cost[-2]
        dp2 = cost[-1]


        for i in range(len(cost) - 3, -1 , -1):

            temp = dp1
            dp1, dp2 = cost[i] + min(dp1, dp2), dp1
    
        
        return min(dp1, dp2)