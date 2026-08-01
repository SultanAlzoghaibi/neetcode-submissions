class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tStk = [] # pair: [temp, index]
        res = [0] * len(temperatures)


        for i, num in enumerate(temperatures):
            while tStk and num > tStk[-1][0]:
                stkT, stkI = tStk.pop()
                res[stkI] =  i  - stkI
                
            tStk.append([num, i])
        
        return res






        