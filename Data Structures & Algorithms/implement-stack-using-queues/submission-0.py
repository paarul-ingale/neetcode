class MyStack:

    def __init__(self):
        self.ans=[]
        

    def push(self, x: int) -> None:
        self.ans.append(x)

    def pop(self) -> int:
        return self.ans.pop()

    def top(self) -> int:
        return self.ans[-1]

    def empty(self) -> bool:
        if self.ans:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()