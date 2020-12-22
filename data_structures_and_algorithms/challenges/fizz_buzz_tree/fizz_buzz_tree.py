class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

def FizzBuzz(data):
    if data % 5 == 0 and data % 3 == 0:
        return "FizzBuzz"
    if data % 3 == 0:
        return "Fizz"
    if data % 5 == 0:
        return "Buzz"
    else:
        return str(data)

def FizzBuzzTree(tree):

    new_tree = BinaryTree()

    if tree.root is None:
        return new_tree

    def finall(cur):
        node = Node(FizzBuzz(cur.data))
        if cur.left:
            node.left = finall(cur.left)
        if cur.right:
            node.right = finall(cur.right)
        return node
    new_tree.root = finall(tree.root)
    return new_tree

if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(6)
    tree.root.left = Node(-3)
    tree.root.right = Node(7)
    tree.root.left.left = Node(15)
    tree.root.left.right = Node(25)