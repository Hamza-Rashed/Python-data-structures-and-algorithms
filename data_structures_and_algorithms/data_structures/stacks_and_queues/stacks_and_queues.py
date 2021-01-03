class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def check_data(self):
        if self.top is None:
            raise Exception("Stack is Empty")
        else:
            while self.top is not None:
                print(self.top.data)
                self.top = self.top.next

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        self.top = self.top.next

    def peek(self):
        return self.top.data

    def isEmpty(self):
        if self.top:
            return False
        return True

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)

        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node

    def dequeue(self):
        self.front = self.front.next

    def peek(self):
        try:
            return self.front.value
        except AttributeError:
            return 'Queue is empty'

    def is_empty(self):
        if self.rear:
            return False
        return True



if __name__ == '__main__':
    main = Stack()
    main.push(1)
    main.push(2)
    main.push(5)
    main.push(10)
    # main.pop()
    # main.pop()
    main.isEmpty()
    main.check_data()