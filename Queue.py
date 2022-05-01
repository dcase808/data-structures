from collections import deque

class Queue():
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None
    
    def peek(self):
        if len(self.queue) > 0:
            return self.queue[-1]
        else:
            return None

    def clear(self):
        self.queue = []

    def __str__(self):
        return str(list(self.queue))
