class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None
    
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
        if self.size == 0:
            self.root = Node(data)
            self.size += 1
            return self.root
        node = self.root
        while node.next != None:
            node = node.next
        node.next = Node(data)
        self.size += 1
        return node.next
    
    def remove(self, data):
        if self.size == 0:
            return None
        
        node = self.root

        if node.data == data:
            self.root = node.next
            self.size -= 1
            return data

        while node.next != None:
            if node.next.data == data:
                node.next == node.next.next
                self.size -= 1
                return data
            node = node.next
        
        return None
    
    def find(self, data):
        if self.size == 0:
            return None
        
        is_next_none = False
        node = self.root

        while not is_next_none:
            if node.data == data:
                return data
            is_next_none = node.next == None
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
