from data_structures_and_algorithms.data_structures.tree.tree import Node, BinaryTree

def test_breadth_first_traversal1():
    bt = BinaryTree()
    bt.root = Node(2) 
    bt.root.left = Node(7) 
    bt.root.right = Node(5) 
    bt.root.left.left = Node(2) 
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    assert bt.breadthFirst(bt.root) == [2,7,5,2,6,9,5,11,4]