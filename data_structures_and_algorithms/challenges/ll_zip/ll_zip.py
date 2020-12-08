
def zipLists(list1, list2):

    First_current = list1.head
    Second_current = list2.head

    if not First_current:
        list1.head = list2.head
        return list1.head

    if not Second_current:
        return list1.head

    step = Second_current.next

    while First_current.next and Second_current.next:
        First_current.next, Second_current.next = Second_current, First_current.next
        First_current = Second_current.next
        Second_current, step = step, step.next

    if not First_current.next:
        First_current.next = Second_current
        return list1.head

    if not Second_current.next:
        First_current.next, Second_current.next = Second_current, First_current.next
        return list1.head
