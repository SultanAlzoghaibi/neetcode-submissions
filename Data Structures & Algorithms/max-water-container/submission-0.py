class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        r = len(heights) - 1
        l = 0
        max_Area = 0

        while l <= r:
            
            w = abs(r - l) 
            h = min(heights[r], heights[l])
            area = w * h

            if max_Area < area:
                max_Area = area

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        
        return max_Area