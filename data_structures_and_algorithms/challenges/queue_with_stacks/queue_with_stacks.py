from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Stack

class PseudoQueue:
    def __init__(self):
        self.stack_one = Stack()
        self.stack_two = Stack()
        self.count = 0

    def enqueue(self, *data):
        self.count += 1 
        for i in data:
            self.stack_one.push(i)

    def dequeue(self):
        if self.stack_two.isEmpty():
            while self.count > 0:
                self.stack_two.push(self.stack_one.pop())
                self.count-=1
            self.stack_two.pop()
            while True:
                self.stack_one.push(self.stack_two.pop())
                self.count +=1
                if self.stack_two.isEmpty():
                    return self.stack_two.pop()
        else:
            return "stack is empty!"

    def __str__(self):
        result = ''
        if self.stack_one.isEmpty():
            current = self.stack_two.top
        else:
            current = self.stack_one.top
        while current:
            result += f"{{{current.data}}} -> "
            current = current.next
        return result

