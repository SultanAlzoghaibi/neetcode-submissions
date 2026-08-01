class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
           return  False 
        for char in s:
            s = s.replace(char,"")
            t = t.replace(char,"")
            if len(s) != len(t):
                return False

        return True




        