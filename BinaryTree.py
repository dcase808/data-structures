from Queue import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)
        self.root.left = Node(9)
        self.root.left.left = Node(7)
        self.root.left.right = Node(8)
        self.root.right = Node(11)
        self.root.right.right = Node(12)

    def depth_first_traversal(self, node):
        if node == None:
            return
        print(node.value)
        self.depth_first_traversal(node.left)
        self.depth_first_traversal(node.right)
        return

    def breadth_first_traversal(self):
        que = Queue()
        que.enqueue(self.root.left)
        que.enqueue(self.root.right)
        print(self.root.value)
        while que.peek():
            node = que.dequeue()
            print(node.value)
            if node.left:
                que.enqueue(node.left)
            if node.right:
                que.enqueue(node.right)

    def flip(self, node):
        if node == None:
            return
        node.left, node.right = node.right, node.left
        self.flip(node.left)
        self.flip(node.right)

    def find(self, value):
        que = Queue()
        que.enqueue(self.root.left)
        que.enqueue(self.root.right)
        while que.peek():
            node = que.dequeue()
            if node.value == value:
                return True
            if node.left:
                que.enqueue(node.left)
            if node.right:
                que.enqueue(node.right)
        return False
    
    def sum(self):
        que = Queue()
        que.enqueue(self.root.left)
        que.enqueue(self.root.right)
        sum = 0
        while que.peek():
            node = que.dequeue()
            sum += node.value
            if node.left:
                que.enqueue(node.left)
            if node.right:
                que.enqueue(node.right)
        return sum