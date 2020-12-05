class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
 
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        node_n = Node(data)

        if not self.head:
            self.head = node_n
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node_n

    def includes(self,data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    

    def __str__(self):
        data = ""
        current = self.head
        while current:
            data += f'{ {current.data} } -> '
            current = current.next
        data += 'NULL'
        return data


if __name__ == '__main__':
    mainll = LinkedList()
    mainll.insert(1)
    mainll.insert(6)
    mainll.insert(9)
    print(mainll.includes(5))
    print(mainll)