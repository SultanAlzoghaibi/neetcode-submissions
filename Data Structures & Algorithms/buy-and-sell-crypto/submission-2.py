class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''

        we shift the left ptr when right ptr is less then value at l
        we take the max while travesing

        '''




        l,r = 0,1
   

        res = 0

        while r < len(prices):


            if prices[l] > prices[r]:
                l += 1
            
                continue
            
            res = max(res, prices[r] - prices[l])
            r += 1

        return res