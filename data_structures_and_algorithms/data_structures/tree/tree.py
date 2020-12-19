class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        if self.front == None:
            return True
        return False

    def enqueue(self, node):
        new_node = node
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.front.value
        return None

class BinaryTree:
    def __init__(self):
        self._root = None
    def pre_order(self, node=None, arr = None):
        if arr is None:
            arr = []
        node = node or self._root
        arr.append(node.data)
        if node.left:
            self.pre_order(node.left, arr)
        if node.right:
            self.pre_order(node.right, arr)
        return arr

    def in_order(self, node=None, arr = None):
        if arr is None:
            arr = []
        node = node or self._root
        if node.left:
            self.in_order(node.left, arr)
        arr.append(node.data)
        if node.right:
            self.in_order(node.right, arr)
        return arr

    def post_order(self, node=None, arr = []):
        node = node or self._root
        if node.left:
            self.post_order(node.left, arr)
        if node.right:
            self.post_order(node.right, arr)
        arr.append(node.data)
        return arr

class BinarySearchTree(BinaryTree):
    def add(self, data):
        node = Node(data)
        if not self._root:
            self._root = node
            return
        current = self._root
        while True:
            if node.data < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = node
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    return
                    
    def contains(self,data):
        if self._root == None:
            raise "Tree is empty"
        current = self._root
        while current:
            if current.data == data:
                return True
            if current.data > data:
                current = current.left
            else:
                current = current.right
        return False