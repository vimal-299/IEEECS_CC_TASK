from collections import deque

class stacks:
    def __init__(self):
        self.stack = deque()
        self.max_stack = deque()
        self.min_stack = deque()
    def push(self,x):
        self.stack.append(x)
        if not self.max_stack or x>self.max_stack[-1]:
            self.max_stack.append(x)
        if not self.min_stack or x<self.min_stack[-1]:    
            self.min_stack.append(x)
    def pop(self):
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        self.stack.pop()
    def top(self):
        print(self.stack[-1])
    def getMin(self):
        if self.min_stack:
            print(self.min_stack[-1])
    def getMax(self):
        if self.max_stack:
            print(self.max_stack[-1])
