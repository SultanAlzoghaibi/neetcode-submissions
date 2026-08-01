class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1hash = {}
        for char in s1:
            if char in s1hash:
                s1hash[char] += 1
            else:
                s1hash[char] = 1
    
        tempS1hash = s1hash.copy()
        l,r = 0,0

        while r < len(s2):
            tempS1hash = s1hash.copy() 
            print(f"l: {l} | r: {r} | tempS1hash: {tempS1hash}")
            
            if s2[l] not in s1hash:
                l += 1
                r += 1
            else:
                
                while r < len(s2) and s2[r] in tempS1hash:
                    print(f"WHILE s2[r] = {s2[r]} | l: {l} | r: {r} | tempS1hash: {tempS1hash}")

                    tempS1hash[s2[r]] -= 1
                    if tempS1hash[s2[r]] == 0:
                        tempS1hash.pop(s2[r])
                

                    r += 1
                    if not tempS1hash:
                        return True
                        
                    if r - l == len(s1):
                        return True
                
                l += 1
                r = l
            

                
        return False