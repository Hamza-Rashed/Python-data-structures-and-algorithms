from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Stack, Queue
import pytest

"""
 ***  queue cases  ***
    1. Can successfully enqueue into a queue
    2. Can successfully enqueue multiple values into a queue
    3. Can successfully dequeue out of a queue the expected value
    4. Can successfully peek into a queue, seeing the expected value
    5. Can successfully empty a queue after multiple dequeues
    6. Can successfully instantiate an empty queue
    7. Calling dequeue or peek on empty queue raises exception
"""

def test_enqueue_one():
    que = Queue()
    que.enqueue(33)
    assert que.rear.data == 33

def test_enqueue_multiple():
    que = Queue()
    que.enqueue(33)
    que.enqueue(5)
    assert que.rear.data == 5
    assert que.front.data == 33

def test_dequeue():
    que = Queue()
    que.enqueue(33)
    que.enqueue(5)
    que.dequeue()
    assert que.front.data == 5

def test_is_empty():
    que = Queue()
    que.enqueue(33)
    que.enqueue(5)
    que.dequeue()
    que.dequeue()
    assert que.is_empty() == False

def test_init():
    que = Queue()
    assert que.front == None
    assert que.rear == None

###############################################

"""
 ***  stack cases  ***
    1. Can successfully push onto a stack
    2. Can successfully push multiple values onto a stack
    3. Can successfully pop off the stack
    4. Can successfully empty a stack after multiple pops
    5. Can successfully peek the next item on the stack
    6. Can successfully instantiate an empty stack
    7. Calling pop or peek on empty stack raises exception
"""

def test_push_one():
    stack = Stack()
    stack.push(33)
    assert stack.top.data == 33


def test_push_multiple():
    stack = Stack()
    stack.push(33)
    stack.push(5)
    assert stack.top.data == 5

def test_pop():
    stack = Stack()
    stack.push(33)
    stack.push(5)
    stack.pop()
    assert stack.top.data == 33

def test_pop_empty():
    stack = Stack()
    stack.push(33)
    stack.push(5)
    stack.pop()
    stack.pop()
    assert stack.isEmpty() == True

def test_stack_peek():
    stack = Stack()
    stack.push(33)
    stack.push(5)
    assert stack.peek() == 5

def test_stack_init():
    stack = Stack()
    assert stack.top == None

def test_stack_empty_exception():
    stack = Stack()
    with pytest.raises(Exception):
        assert stack.pop()
    with pytest.raises(Exception):
        assert stack.peek()