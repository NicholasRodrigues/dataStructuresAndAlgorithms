class Stack:
    def __init__(self):
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack)-1]

    def push(self, value):
        self.stack.append(value)
        return self

    def pop(self):
        return self.stack.pop()


