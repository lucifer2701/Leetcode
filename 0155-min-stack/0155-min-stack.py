class MinStack:

    def __init__(self):
        self.minstack=[]
        self.stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack and self.minstack[-1]>=val or not self.minstack:
            self.minstack.append(val)

    def pop(self) -> None:
        v=self.stack.pop()
        if v==self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()