from data_structures_and_algorithms.data_structures.tree.tree import Node, BinaryTree, Queue
import pytest


def test_find_max_binarytree_empty():
    tree = BinaryTree()
    assert tree.find_maximum_value() == None


def test_find_max_binarytree_zeros():
    tree = BinaryTree()
    tree._root = Node(-2)
    tree._root.left = Node(-4)
    tree._root.right = Node(0)
    assert tree.find_maximum_value() == 0

def test_find_max_binarytree_one_el():
    tree = BinaryTree()
    tree._root = Node(8)
    assert tree.find_maximum_value() == 8

def test_find_max_binarytree_several_el():
    tree = BinaryTree()
    tree._root = Node(8)
    tree._root.left = Node(10)
    tree._root.right = Node(-2)
    assert tree.find_maximum_value() == 10
    tree._root.left.left = Node(195)
    tree._root.left.right = Node(-195)
    tree._root.right.right = Node(10000)
    tree._root.left.left.left = Node(-0.567)
    tree._root.left.left.right = Node(10000)
    assert tree.find_maximum_value() == 10000

def test_find_max_binarytree_same_values():
    tree = BinaryTree()
    tree._root = Node(-2)
    tree._root.left = Node(-2)
    tree._root.right = Node(-2)
    tree._root.left.left = Node(-2)
    tree._root.left.right = Node(-2)
    tree._root.right.right = Node(-2)
    tree._root.left.left.left = Node(-2)
    tree._root.left.left.right = Node(-2)
    assert tree.find_maximum_value() == -2
    tree._root.right.left = Node(1)
    assert tree.find_maximum_value() == 1

def test_find_max__imbalanced_binarytree():
    tree = BinaryTree()
    tree._root = Node(-2)
    tree._root.left = Node(5)
    tree._root.left.left = Node(9)
    tree._root.left.left.left = Node(2)
    tree._root.left.left.left.left = Node(2)
    assert tree.find_maximum_value() == 9