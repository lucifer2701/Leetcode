class MinStack:

    def __init__(self):
        self.stack=[]
        self.s=[]
        

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.stack and self.stack[-1]>=val or not self.stack:
            self.stack.append(val)

    def pop(self) -> None:
        v=self.s.pop()
        if v==self.stack[-1]:
            self.stack.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()