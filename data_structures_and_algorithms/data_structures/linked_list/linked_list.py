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

    def append(self, data):

        node_n = Node(data)
        current = self.head
        if not self.head:
            self.head = node_n
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_n

    def insertBefore(self, data, newVal):

        current = self.head
        print(current.next)
        while current is not None:
            if current.data == data:
                break
            current = current.next
        if current is None:
            print("Exception: the value not exisit in the linked list")
        else:
            new_node = Node(newVal)
            new_node.next = current.next
            current.next = new_node 
            
    def insertAfter(self, data, newVal):
        node_n = Node(newVal)
        current = self.head
        if not self.head:
                self.head = node_n
        else:
            current = self.head
            while current:
                if current.next != None:
                    if current.data == data:
                        next_d = current.next
                        current.next = node_n
                        node_n.next = next_d
                        return newVal
                    else:
                        current = current.next
                else:
                    current.next = node_n
                    return newVal
            return "this node donsen't exist!"

    
    def delete_value(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return "done!"
        else:
            current = self.head
            while current:
                if current.next.data == data:
                    current.next = current.next.next
                    return "done!"
                current = current.next
if __name__ == '__main__':
    free_all = LinkedList()
    free_all.insert(1)
    free_all.insert(6)
    free_all.insert(9)
    print(free_all.includes(5))
    print(free_all)
