class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        stk = [] # [ [idx, height]]

        res = [0]
        for i, h in enumerate(heights):
            
            start = i
            while stk and stk[-1][1] > h:

                topI, topH = stk.pop()
                res[0] = max(res[0], abs(topI - i) * topH)
                start = topI

            stk.append((start, h))
        
        for currI, currH in stk:
            res[0] = max(res[0], abs(len(heights) - currI) * currH)

        return res[0]


            
