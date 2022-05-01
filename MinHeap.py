class MinHeap():
    def __init__(self, items):
        self.heap = []
        self.heap.append(0)
        for index, item in enumerate(items):
            self.heap.append(item)
            self.__bubble_up(index + 1)
    
    def push(self, item):
        self.heap.append(item)
        self.__bubble_up(len(self.heap) - 1)
    
    def pop(self):
        if len(self.heap) < 2:
            return None
        elif len(self.heap) == 2:
            return self.heap.pop()
        else:
            self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
            self.heap.pop()
            self.__bubble_down(1)
    
    def peek(self):
        if self.heap[0]:
            return self.heap[0]
        return None

    def __bubble_up(self, index):
        if index == 1:
            return
    
        parent = index // 2

        if self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.__bubble_up(parent)
    
    def __bubble_down(self, index):
        left, right = index * 2, index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[index] > self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] > self.heap[right]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.__bubble_down(largest)

    def __str__(self):
        return str(self.heap[1:])
