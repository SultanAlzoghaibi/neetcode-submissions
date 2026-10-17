class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''

        AABAACBB
        window ={A:2,C:1}


        diffSet = set()
        size of the diffSet = k + 1

        k = 1
        kleft = 0
        l = 0
        r = 2
        '''


        window = defaultdict(int)
        #
        l = 0

        kleft = k
        res = 0
        maxFreq = 0
        for r, c in enumerate(s):
            #print(window, r,c, maxFreq)

            window[c] += 1
          
            maxFreq = max(maxFreq, window[c])

            while (r - l + 1)  - maxFreq > k:
                window[s[l]]  -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1

            res = max(res, r - l + 1)
        #print(window)


       
        return res
