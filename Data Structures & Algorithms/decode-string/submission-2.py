class Solution:
    def decodeString(self, s: str) -> str:
        '''
        f 2[a3[b]]c
        stk = [2,
        res = a,b,b,b
        a) save position to know what to dublicate.

        b) while loop till interger once we encounter a ]
        stk = 2 a bbb 
        res = stk

        '''
        stk = []
        for c in s:
            #print(stk, c)
            
            if c != ']' :
                stk.append(c)
                continue
            
            multiplyStr = []
            while stk and stk[-1] != '[':
                multiplyStr.append(stk.pop())
            stk.pop()
            #print("multiplyStr:", multiplyStr)
            # num calc 123
            multiplyer = 0

            i = 1 
            while stk and stk[-1].isnumeric():
                multiplyer += int(stk.pop()) * i
                i *= 10
            # create the string
            stk.append("".join(reversed(multiplyStr)) * multiplyer)

        return "".join(stk)
     

            


        