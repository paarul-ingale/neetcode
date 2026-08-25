class FreqStack:

    def __init__(self):
        self.stack=[]
        self.freq={}

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        self.stack.append(val)
        

    def pop(self) -> int:
        if not self.stack:
            return 0
        newstack = []
        max_freq = max(self.freq.values())
        max_values = [x for x in self.freq if self.freq[x] == max_freq]

        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i] in max_values:
                frequent_no = self.stack[i]
                self.freq[frequent_no] -= 1
                self.stack.pop()
                break
            else:
                newstack.append(self.stack.pop())

        while newstack:
            self.stack.append(newstack.pop())
        return frequent_no
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()