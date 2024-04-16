class Stack:

    def __init__(self):
        self.newStack = []

    def push(self, item):
        self.newStack.append(item)
        return self.newStack

    def pop(self):
        self.newStack.pop()
        return self.newStack

    def empty(self):
        return len(self.newStack) == 0

    def peek(self):
        if self.newStack:
            item = self.newStack[-1]
            return item
        else:
            print("Stack is empty")

    def size(self):
        return len(self.newStack)