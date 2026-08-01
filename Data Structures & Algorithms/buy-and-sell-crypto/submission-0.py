class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        r = 0
        l = 0

        while r < len(prices) - 1:
            r = r + 1

            if(prices[l] > prices[r]):
                l = r
            
            Profit = (prices[r] - prices[l])

            if Profit > maxProfit:
                maxProfit = Profit
        
        return maxProfit
        