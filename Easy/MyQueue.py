class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []
    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()
        
    def peek(self) -> int:
        while self.input:
            if not self.pop:
                self.output.append(self.input.pop())
            else:
                return self.output[-1]    
        return self.output[-1]
    
    def empty(self) -> bool:
        if self.input or self.output:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()