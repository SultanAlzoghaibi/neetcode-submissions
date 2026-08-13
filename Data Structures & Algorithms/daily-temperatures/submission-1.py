class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stk = [] # num, pos
        ### 
        res = [0] * len(temperatures)
        for i, n in enumerate(temperatures):

            while stk and n > stk[-1][0]:
                stackT, stackInd = stk.pop()
                res[stackInd] = i - stackInd

            stk.append((n, i))
        return res
            
        