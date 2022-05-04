from copy import copy
from Queue import Queue
from Stack import Stack

class Graph:
    def __init__(self, graph):
        self.graph = graph
    
    def __str__(self):
        return str(self.graph)

    def depth_first_traversal(self, start):
        graph = copy(self.graph)
        stack = Stack()
        stack.push(start)
        visited = set()
        print('start', end=' -> ')
        while stack.peek():
            first_element = stack.pop()
            if first_element not in visited:
                visited.add(first_element)
                print(first_element, end=' -> ')
                for el in graph[first_element]:
                    stack.push(el)
        print('end')
        return visited

    def breadth_first_traversal(self, start):
        graph = copy(self.graph)
        que = Queue()
        que.enqueue(start)
        visited = set()
        print('start', end=' -> ')
        while que.peek():
            first_element = que.dequeue()
            if first_element not in visited:
                visited.add(first_element)
                print(first_element, end=' -> ')
                for el in graph[first_element]:
                    que.enqueue(el)
        print('end')
        return visited
    
    def is_there_way(self, start, destination):
        graph = copy(self.graph)
        stack = Stack()
        stack.push(start)
        visited = set()
        while stack.peek():
            first_element = stack.pop()
            if first_element == destination:
                return True
            if first_element not in visited:
                visited.add(first_element)
                for el in graph[first_element]:
                    stack.push(el)
        return False
    
    def count_connected_components(self):
        graph = copy(self.graph)
        visited = set()
        count = 0
        
        for key in graph.keys():
            if key not in visited:
                vis = self.depth_first_traversal(key)
                visited = visited.union(vis)
                count += 1
        return count
    
    def largest_component(self):
        graph = copy(self.graph)
        visited = set()
        largest = 0
        largest_set = set()
        count = 0
        
        for key in graph.keys():
            if key not in visited:
                vis = self.depth_first_traversal(key)
                if len(vis) > largest:
                    largest = len(vis)
                    largest_set = vis
                visited = visited.union(vis)
                count += 1
        return largest, largest_set

    def shortest_path(self, start, end):
        graph = copy(self.graph)
        que = Queue()
        visited = set()
        distance_from_start = 0
        que.enqueue((start, 0))

        while que.peek():
            first_element = que.dequeue()[0]
            if first_element not in visited:
                visited.add(first_element)
                distance_from_start += 1
                for el in graph[first_element]:
                    if el == end:
                        return distance_from_start
                    que.enqueue((el, distance_from_start))
        return False