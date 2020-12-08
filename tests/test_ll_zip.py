from data_structures_and_algorithms.data_structures.linked_list.linked_list import LinkedList,Node
from data_structures_and_algorithms.challenges.ll_zip.ll_zip import zipLists

def test_equal_list():
    First_test = LinkedList()
    Second_test = LinkedList()
    
    First_test.append(1)
    First_test.append(3)
    First_test.append(2)
    
    Second_test.append(5)
    Second_test.append(9)
    Second_test.append(4)
   
    
    zipLists(First_test,Second_test)
    expected = "{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> NULL"
    actual = First_test.__str__()
    assert expected == actual

def test_not_equal_first_list():
    First_test = LinkedList()
    Second_test = LinkedList()
    
    First_test.append(1)
    First_test.append(3)
    
    Second_test.append(5)
    Second_test.append(9)
    Second_test.append(4)
    
    zipLists(First_test,Second_test)
    expected = "{1} -> {5} -> {3} -> {9} -> {4} -> NULL"
    actual = First_test.__str__()
    assert expected == actual

def test_not_equal_second_list():
    First_test = LinkedList()
    Second_test = LinkedList()
    
    First_test.append(1)
    First_test.append(3)
    First_test.append(2)
    
    Second_test.append(5)
    Second_test.append(9)
    
    zipLists(First_test,Second_test)
    expected = "{1} -> {5} -> {3} -> {9} -> {2} -> NULL"
    actual = First_test.__str__()
    assert expected == actual