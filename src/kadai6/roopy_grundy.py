from adjacency_list import GameGraph

def mex(integer_set):
    integer_list = list(integer_set)
    i = 0
    while True:
        if i not in integer_list:
            return i
        i += 1

def initialize_grundy_numbers(game_graph: GameGraph):
    """Initialize Grundy numbers for all nodes in the game graph"""
    grundy_numbers = []

    for adjacent_nodes in game_graph.nodes:
        if len(adjacent_nodes) == 0:
            # Terminal state (no adjacent nodes)
            grundy_numbers.append(0)
        else:
            # Non-terminal state
            grundy_numbers.append(float("inf"))

    return grundy_numbers

def m_n(game_graph: GameGraph, node, grundy_numbers):
    # set adjacency grundy numbers set
    adj_grundy_set = set()

    for next_node in game_graph.nodes[node]:
        grundy_number = grundy_numbers[next_node]
        adj_grundy_set.add(grundy_number)

    # calculate mex
    return mex(adj_grundy_set)


def calculate_n_grundy_number(game_graph: GameGraph, node, grundy_numbers):    
    if grundy_numbers[node] != float("inf"):
        return grundy_numbers[node]
    else:
        node_m_n = m_n(game_graph, node, grundy_numbers)

        for next_node in game_graph.nodes[node]:
            if grundy_numbers[next_node] > node_m_n:
                is_exist_next_next_node = False

                for next_next_node in game_graph.nodes[next_node]:
                    if grundy_numbers[next_next_node] == node_m_n:
                        is_exist_next_next_node = True # update is_exist_next_next_node
                        break
                
                if not is_exist_next_next_node:
                    return float("inf")
                    
        return node_m_n
    
def calculate_n_grundy_numbers(game_graph: GameGraph, grundy_numbers):
    # initialize new grundy_numbers
    new_grundy_numbers = []

    for node, _ in enumerate(game_graph.nodes):
        grundy_number = calculate_n_grundy_number(game_graph, node, grundy_numbers)
        new_grundy_numbers.append(grundy_number)

    return new_grundy_numbers
    