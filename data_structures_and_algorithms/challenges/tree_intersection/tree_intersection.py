from data_structures_and_algorithms.data_structures.tree.tree import BinarySearchTree, BinaryTree, Node

def tree_intersection(tree1, tree2):

    result = []
    first = tree1.breadth_first_traversal()
    second = tree2.breadth_first_traversal()
    for x in range(len(first)):
        if first[x] == second[x]:
            result.append(first[x])
    if len(result) > 0:
        return result
    else:
        return None
