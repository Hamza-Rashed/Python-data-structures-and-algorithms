from data_structures_and_algorithms.challenges.fizz_buzz_tree.fizz_buzz_tree import *
import pytest

@pytest.fixture
def my_tree():
    tree = BinaryTree()
    tree.root = Node(6)
    tree.root.left = Node(-3)
    tree.root.right = Node(7)
    tree.root.left.left = Node(15)
    tree.root.left.right = Node(25)
    return tree

def test_fizz_buzz7(my_tree):
    tree_test = my_tree
    new_tree = FizzBuzzTree(tree_test)
    assert new_tree.root.right.data == "7"

def test_fizz_buzz_third(my_tree):
    tree_test = my_tree
    new_tree = FizzBuzzTree(tree_test)
    assert new_tree.root.left.right.data == "Buzz"

def test_empty_tree():
    tree = BinaryTree()
    new_tree = FizzBuzzTree(tree)
    assert new_tree.root == None