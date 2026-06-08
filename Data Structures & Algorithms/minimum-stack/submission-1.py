class MinStack:

    def __init__(self):
       #decreasing stack
       self.minstack=[]
       self.mainstack=[]


    def push(self, val: int) -> None:
        self.mainstack.append(val)
        if self.minstack and self.mainstack[-1]>self.minstack[-1]:
            self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(val)
        
    def pop(self) -> None:
        self.mainstack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.mainstack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
