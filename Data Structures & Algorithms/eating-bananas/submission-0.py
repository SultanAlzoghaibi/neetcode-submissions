class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1 
        r = max(piles)
        res = r

        while l <= r:
            midk = (l + r) // 2

            totatTime = 0
            for p in piles:
                totatTime += math.ceil(float(p) / midk)
            
            if totatTime <= h:
                res = min(res, midk)
                r = midk - 1
            else:
                l = midk + 1

        return res

            


