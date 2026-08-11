class MinStack:
    

    def __init__(self):
        self.ans=[]
        self.minimum = []

    def push(self, val: int) -> None:
        
        self.ans.append(val)
        if not self.minimum:
            self.minimum.append(val)
        else:
            self.minimum.append(min(val , self.minimum[-1]))        

    def pop(self) -> None:
        
        self.ans.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.ans[-1]

    def getMin(self) -> int:
        return self.minimum[-1]