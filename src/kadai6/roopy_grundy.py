from adjacency_list import GameGraph

def mex(integer_set):
    """
    Calculate mex which defined mex(integer_set) = min({i | i not in integer_set})

    Parameters
    -------
    integer_set: set
        Set included N.
        In this module, set is grundy numbers of G's next node.

    Returns
    -------
    i: int
        mex of integer_sets
    """
    integer_list = list(integer_set)
    i = 0
    while True:
        if i not in integer_list:
            return i
        i += 1

def initialize_grundy_numbers(game_graph: GameGraph):
    """
    Initialize grundy numbers of game_graph.

    Parameters
    -------
    game_graph: GameGraph
        The game_graph which is calculate grundy numbers

    Returns
    -------
    grundy_numbers: list
        Initialized grundy numbers.
    """
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
    """
    Calculate mex of Grundy numbers of a given node's adjacent nodes.

    Parameters
    ----------
    game_graph : GameGraph
        The game graph which is expressed as adjacency list.
    node : int
        The target node index for which to calculate mex.
    grundy_numbers : list
        List of current Grundy numbers for all nodes.

    Returns
    -------
    int
        The mex (minimum excludant) value of adjacent nodes' Grundy numbers.
    """
    # set adjacency grundy numbers set
    adj_grundy_set = set()

    for next_node in game_graph.nodes[node]:
        grundy_number = grundy_numbers[next_node]
        adj_grundy_set.add(grundy_number)

    # calculate mex
    return mex(adj_grundy_set)


def calculate_n_grundy_number(game_graph: GameGraph, node, grundy_numbers):
    """
    Calculate the Grundy number for a single node using the loopy Grundy algorithm.

    Parameters
    ----------
    game_graph : GameGraph
        The game graph which is expressed as adjacency list.
    node : int
        The target node index for which to calculate Grundy number.
    grundy_numbers : list
        List of current Grundy numbers for all nodes.

    Returns
    -------
    int or float
        The calculated Grundy number for the node, or float("inf") if undetermined.
    """
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
    """
    Calculate Grundy numbers for all nodes in the graph using one iteration.

    Parameters
    ----------
    game_graph : GameGraph
        The game graph which is expressed as adjacency list.
    grundy_numbers : list
        List of current Grundy numbers for all nodes.

    Returns
    -------
    list
        Updated list of Grundy numbers for all nodes.
    """
    # initialize new grundy_numbers
    new_grundy_numbers = []

    for node, _ in enumerate(game_graph.nodes):
        grundy_number = calculate_n_grundy_number(game_graph, node, grundy_numbers)
        new_grundy_numbers.append(grundy_number)

    return new_grundy_numbers

def calculate_grundy_numbers(game_graph: GameGraph):
    """
    Calculate the final Grundy numbers for all nodes using iterative loopy Grundy algorithm.

    This function iteratively calculates Grundy numbers until convergence is reached.
    The algorithm handles cycles in the game graph by using the loopy Grundy approach.

    Parameters
    ----------
    game_graph : GameGraph
        The game graph which is expressed as adjacency list.

    Returns
    -------
    list
        Final list of Grundy numbers for all nodes in the graph.
    """
    pre_grundy_numbers = initialize_grundy_numbers(game_graph)

    while True:
        current_grundy_numbers = calculate_n_grundy_numbers(game_graph, pre_grundy_numbers)

        if current_grundy_numbers == pre_grundy_numbers:
            return current_grundy_numbers

        pre_grundy_numbers = current_grundy_numbers        
    