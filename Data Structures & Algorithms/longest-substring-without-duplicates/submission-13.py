class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        xzyzxyz
        last = 2
        map = {'x':0,'z':1}
        '''

        seen = {}
        l = 0
        if s == "":
            return 0
        res = 0

        for i, c in enumerate(s):
            #print(l,i,c,seen,)
            if c in seen:
                
                l = max(l, seen[c] + 1)
           
        
            
            res = max(res, i - l + 1) 
            seen[c] = i


           
        
        return res
        