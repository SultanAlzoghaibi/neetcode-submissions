class FreqStack:

    def __init__(self):
        self.stkOfStks = {} # countGroup: [stk]
        self.maxCnt = 0
        self.cntMap = {} # val : cnt


      

        

    def push(self, val: int) -> None:
        newCnt = self.cntMap.get(val, 0) + 1
        self.cntMap[val] = newCnt

        if newCnt > self.maxCnt:
            self.maxCnt = newCnt
            self.stkOfStks[newCnt] = []

        self.stkOfStks[newCnt].append(val)



     
    def pop(self) -> int:
        res = self.stkOfStks[self.maxCnt].pop()
        self.cntMap[res] -= 1
        if not self.stkOfStks[self.maxCnt]:
            self.maxCnt -= 1
        return res
        
        


'''
from the 

pushcnt = 0 # every push will increment this 
maxHeap = (freq, val)
lastAddedMap = {val, stk[0,1,2 ]} #stk -> pushcnt 

when theres a tie:
    for check lastAddedMap of ecah val use the one with the greatest pushcnt poping that number from the vals keys -> stk

    stk
    freqmap
    { val: indexStk }



'''


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()