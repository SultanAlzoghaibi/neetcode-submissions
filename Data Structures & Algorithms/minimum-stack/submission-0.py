class MinStack:
    def __init__(self):
        self.orderStk = []
        self.minStk = []

    def push(self, val: int) -> None:
        self.orderStk.append(val)
        if not self.minStk or val <= self.minStk[-1]:
            self.minStk.append(val)
        else:
            self.minStk.append(self.minStk[-1])
        
    def pop(self) -> None:
        self.orderStk.pop()
        self.minStk.pop()

    def top(self) -> int:
        top = self.orderStk[-1]
        return top

    def getMin(self) -> int:
        top = self.minStk[-1]
        return top


        
