class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize        

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        stack_two = []
        
        while self.stack:
            stack_two.append(self.stack.pop())
            
        i = 0
        while stack_two:
            if i < k:
                self.stack.append(stack_two.pop()+val)
                i += 1
            else:
                self.stack.append(stack_two.pop())
            
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)