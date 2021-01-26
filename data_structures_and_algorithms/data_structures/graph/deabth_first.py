from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Stack , Queue , Node

def depth_first(self, starting_vertex):
    vertices = []
    depth = Stack()

    if starting_vertex not in self._adjacency_list:
        raise ValueError
    
    depth.push(starting_vertex)

    while not depth.is_empty():
        top_vertex = depth.pop()
        vertices.append(top_vertex.value)
        top_node_neighbors = self.get_neighbors(top_vertex)

        for neighbor in top_node_neighbors[::-1]:
            if not neighbor[0].visited:
                top_vertex.visited = True
                neighbor[0].visited = True

                depth.push(neighbor[0])

    for node in self._adjacency_list:
        node.visited = False

    return vertices
