# Tree
BinaryTree():

.pre_order() - BinaryTree method to return an array of trre values in "pre-order" order
.in_order() - BinaryTree method to return an array of tree values "in-order"
.post_order() - BinaryTree method to return an array of tree values "post-order
BinarySearchTree(BinaryTree):

.add(value) - BinarySearchTree method that accepts a value, and adds a new node with that value in the correct location in the binary search tree
.contains(value) - BinarySearchTree method that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

### Cases : 

* Can successfully instantiate an empty tree
* Can successfully instantiate a tree with a single root node
* Can successfully add a left child and right child to a single root node
* Can successfully return a collection from a preorder traversal
* Can successfully return a collection from an inorder traversal
* Can successfully return a collection from a postorder traversal

![](https://raw.githubusercontent.com/Hamza-Rashed/Python-data-structures-and-algorithms/main/asset/tree.jpeg)

[PR](https://github.com/Hamza-Rashed/Python-data-structures-and-algorithms/pull/17)

# Find the Maximum Value in a Binary Tree
## Challenge
Write an instance method called find-maximum-value. Without utilizing any of the built-in methods, return the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Approach & Efficiency
Time Big O(n) Space Big O(W) where W - Width of the tree because we are using Queue through traversiong of our tree

![](https://raw.githubusercontent.com/Hamza-Rashed/Python-data-structures-and-algorithms/main/asset/find_maximum_binary_tree.jpeg)

[PR](https://github.com/Hamza-Rashed/Python-data-structures-and-algorithms/pull/18)

# Breadth First
## Challenge
Write a breadth first traversal method which takes a Binary Tree as its unique input. Without utilizing any of the built-in methods available to your language, traverse the input tree using a Breadth-first approach, and return a list of the values in the tree in the order they were encountered.

## Approach & Efficiency
Time Big O(n) Space Big O(n)


![](https://raw.githubusercontent.com/Hamza-Rashed/Python-data-structures-and-algorithms/main/asset/%D9%A2%D9%A0%D9%A2%D9%A0%D9%A1%D9%A2%D9%A2%D9%A1_%D9%A2%D9%A0%D9%A1%D9%A1%D9%A5%D9%A8%5B1%5D.jpg)

[PR](https://github.com/Hamza-Rashed/Python-data-structures-and-algorithms/pull/19)

