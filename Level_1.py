from collections import deque

class stacks:

    def __init__(self):
        self.stack = deque()  # creating the main stack
        self.max_stack = deque()  # creating a stack to keep track of max values
        self.min_stack = deque()  # creatign a stack to keep track of min values

    def push(self,x):
        self.stack.append(x)  # Pushes the element 'x' to the top of the stack
        if not self.max_stack or x>self.max_stack[-1]:
            self.max_stack.append(x)  # If 'x' is bigger than the previous number it will add x to max_stack
        if not self.min_stack or x<self.min_stack[-1]:    
            self.min_stack.append(x)  # If 'x' is smaller than the previous number it will add x to min_stack

    def pop(self):
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()  # Removes the top most element of max_stack if it is the max value
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()  # Removes the top most element of min_stack if it is the min value
        self.stack.pop()  # Removes the top most element of the stack

    def top(self):
        return(self.stack[-1])  # Returns the top most element of the stack without removing it
    
    def getMin(self):
        if self.min_stack:   # checks if the min_stack is empty or not 
            return(self.min_stack[-1])  # If not empty, it will return min value of the stack
        else :
            return("stack is empty")  # If stack is empty it will return 'stack is empty'

    def getMax(self):
        if self.max_stack:  # checks if the max_stack is empty or not
            return(self.max_stack[-1])  # If not empty, it will return max value of the stack
        else:
            return("stack is empty")  # If stack is empty it will return 'stack is empty'
