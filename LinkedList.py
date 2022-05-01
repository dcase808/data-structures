class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return self.data

class LinkedList:
    def __init__(self, root = None):
        if root:
            self.root = Node(root)
            self.size = 1
        else:
            self.root = root
            self.size = 0

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1
        return new_node
    
    def remove(self, data):
        node = self.root
        if node.data == data:
            self.root = node.next
            self.size -= 1
            return data
        
        while node.next is not None:
            if node.next.data == data:
                node.next = node.next.next
                return data
            node = node.next
    
    def find(self, data):
        node = self.root
        while node is not None:
            if node.data == data:
                return data
            node = node.next
        return None

    def __str__(self):
        if self.size == 0:
            return str(None)

        is_next_none = False
        node = self.root
        out = ''

        while not is_next_none:
            out += str(node.data) + ' '
            is_next_none = node.next == None
            node = node.next

        return out
