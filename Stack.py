class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    
    def clear(self):
        self.stack = []
    
    def __str__(self):
        return str(self.stack)
