class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        resMax = [s[0], 0]

        for i in range(len(s)):

            r = l = i
            #odd
            while r < len(s) and l >= 0  and s[l] == s[r]:
                size = r - l + 1

                if size > resMax[1]:
                    resMax[1] = size
                    resMax[0] = s[l:r+1]
                r += 1
                l -=1

            l, r = i, i +1
        
            #even
            while r < len(s) and l >= 0 and s[l] == s[r]:
                size = r - l + 1
                if size > resMax[1]:
                    resMax[1] = size
                    resMax[0] = s[l:r+1]
                r += 1
                l -=1
            
        
        return resMax[0]

