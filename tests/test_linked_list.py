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

@pytest.fixture
def testing():
    linked = LinkedList()
    LinkedList.links = []
    linked = LinkedList()
    linked.insert(3)
    linked.insert(6)
    linked.insert(9)
    return linked