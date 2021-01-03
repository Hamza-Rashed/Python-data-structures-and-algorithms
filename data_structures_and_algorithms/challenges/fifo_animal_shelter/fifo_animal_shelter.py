import copy

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        if self.front == None:
            return True
        return False

    def enqueue(self, data):
        if self.is_empty():
            self.front = data
            self.rear = data
        else:
            self.rear.next = data
            self.rear = data

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
            return self.front.data
        return None

class Animal:
    def __init__(self, data):
        self.data = data
        self.next = None

class Cat(Animal):
    type = 'cat'

class Dog(Animal):
    type = 'dog'

class AnimalShelter:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Cat) or isinstance(animal, Dog):
            self.queue1.enqueue(animal)
        else:
            return "Animal must be cat or dog"

    def dequeue(self, p):
        d_animal = None
        while not self.queue1.is_empty():
            if self.queue1.front.type == p.lower() and d_animal == None:
                d_animal= self.queue1.dequeue()
            else:
                self.queue2.enqueue(self.queue1.dequeue())

        while not self.queue2.is_empty():
            self.queue1.enqueue(self.queue2.dequeue())

        return d_animal
