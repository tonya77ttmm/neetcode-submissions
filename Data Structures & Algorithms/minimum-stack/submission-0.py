class MinStack:

    def __init__(self):
        #[]
        #minvalue
        #topvalue=[-1]
        #pop
        #getmin=[] decreasing stack
        self.minstack=[]
        self.q=[]


    def push(self, val: int) -> None:
        self.q.append(val)
        val=min(val, self.minstack[-1] if self.minstack else val )
        self.minstack.append(val)
    def pop(self) -> None:
        self.minstack.pop()
        self.q.pop()
        

    def top(self) -> int:
        return self.q[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
