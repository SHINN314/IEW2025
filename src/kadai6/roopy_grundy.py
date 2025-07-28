from adjacency_list import GameGraph

def mex(grundy_values_set):
    """Calculate minimum excludant (mex) of a set of Grundy numbers"""
    i = 0
    while True:
        if i not in grundy_values_set:
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

def m_n(game_graph: GameGraph, node):
    return mex(game_graph.nodes[node])

def calculate_grundy_numbers(game_graph: GameGraph, grundy_numbers):
    new_grundy_numbers = []

    for node, node_adj in enumerate(game_graph.nodes):
        if grundy_numbers[node] == float("inf"):
            # update grundy number where the grundy number is infinity
            
            for i, next_node in enumerate(node_adj):
                is_exist_next_node = False

                if grundy_numbers[next_node] > m_n(game_graph, node):
                    # check all next node where g_n(next_node) > m_n(node)
                    is_exist_next_node = True # update next node flag
                    is_exist_next_next_node = False

                    for j, next_next_node in enumerate(game_graph.nodes[next_node]):
                        if grundy_numbers[next_node] == m_n(game_graph, node):
                            new_grundy_numbers.append(m_n(game_graph, node))
                            is_exist_node = True # update next next node flag
                            break

                    if (not is_exist_next_next_node):
                        new_grundy_numbers.append(float("inf"))

            if (not is_exist_next_node):
                new_grundy_numbers.append(m_n(node))

        else:
            new_grundy_numbers.append(grundy_numbers[node])
                    
