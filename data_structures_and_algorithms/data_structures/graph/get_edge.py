from graph import Graph

def dict_node(nodes):
    dict_nodes = {}
    for node in nodes:
        dict_nodes[node.value] = node
    return dict_nodes

def neighbors(nodes):
    neighbors = {}
    for node in nodes:
        neighbors[node[0].value] = node
    return neighbors

def get_edge(graph, arr):

    dict_nodes = dict_node(graph.get_nodes())
    price = 0

    for i in range (0, len(arr)-1):

        if arr[i] not in dict_nodes:
            return False, '$0'

        if arr[i] in dict_nodes:
            neighbors_dict = neighbors(graph.get_neighbors(dict_nodes[arr[i]]))

            if arr[i+1] in neighbors_dict:
                price += neighbors_dict[arr[i+1]][1]

            else:
                return False, '$0'


    return True, f'${price}'