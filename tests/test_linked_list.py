from data_structures_and_algorithms.data_structures.linked_list.linked_list import LinkedList
import pytest


linked_lii = LinkedList()
linked_lii.insert(3)
linked_lii.insert(6)
linked_lii.insert(9)


def test_instance():
    assert isinstance(linked_lii, LinkedList)

def test_insert():
    data = ''
    linked_list = linked_lii.head
    while linked_list:
        data += f'{linked_list.data},'
        linked_list = linked_list.next
    assert data == '3,6,9,'

def test_head():
    assert linked_lii.head.data == 3

def test_head_next():
    assert linked_lii.head.next.next.data == 9

def test_finding_notExist_value():
    assert linked_lii.includes(5) == False

def test_finding_exist_value():
    assert linked_lii.includes(6) == True

def test_string_str():
    assert linked_lii.__str__() == '{3} -> {6} -> {9} -> NULL'

"""

    Can successfully add a node to the end of the linked list
    Can successfully add multiple nodes to the end of a linked list
    Can successfully insert a node before a node located i the middle of a linked list
    Can successfully insert a node before the first node of a linked list
    Can successfully insert after a node in the middle of the linked list
    Can successfully insert a node after the last node of the linked list

"""

def test_append():
    linked_lii.append(11)
    current = linked_lii.head
    while current.next:
        current = current.next
    assert current.next == None
    assert linked_lii.__str__() == '{3} -> {6} -> {9} -> {11} -> NULL'


def test_insertBefore():
    linked_lii.insertBefore(3, 2)
    linked_lii.insertBefore(9, 5)
    actual = linked_lii.__str__()
    expected =  '{3} -> {2} -> {6} -> {9} -> {5} -> {11} -> NULL'
    assert actual == expected

def test_insertBefore_edgeCase():
    linked_lii.insertBefore(12, 4)
    assert "this node is not exist!"


def test_insertAfter():
    linked_lii.insertAfter(9, 10)
    linked_lii.insertAfter(11, 12)
    actual = linked_lii.__str__()
    expected =  '{3} -> {2} -> {6} -> {9} -> {10} -> {5} -> {11} -> {12} -> NULL'
    assert actual == expected

def test_insertAfter_edgeCase():
    linked_lii.insertAfter(1, 10)
    assert "this node dosen't exist!"

def test_delete_node():
    linked_lii.delete_value(12)
    linked_lii.delete_value(11)
    linked_lii.delete_value(10)
    linked_lii.delete_value(10)
    linked_lii.delete_value(5)
    assert linked_lii.__str__() == '{3} -> {2} -> {6} -> {9} -> NULL'
    linked_lii.delete_value(2)
    assert linked_lii.__str__() == '{3} -> {6} -> {9} -> NULL'