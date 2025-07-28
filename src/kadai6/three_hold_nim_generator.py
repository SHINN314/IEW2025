from adjacency_list import GameGraph

def pairing_function(x, y):
    """
    Calculate the Cantor pairing function to map two non-negative integers to a unique integer.
    
    The Cantor pairing function is a bijection from N×N to N, which allows encoding
    two-dimensional coordinates (x, y) into a single unique integer.
    
    Parameters
    ----------
    x : int
        First non-negative integer coordinate.
    y : int
        Second non-negative integer coordinate.
        
    Returns
    -------
    int
        Unique integer representation of the coordinate pair (x, y).
    """
    return (x + y) * (x + y + 1) // 2 + x

def draw_vertical_edges(x, y):
    """
    Generate all possible vertical moves from position (x, y) in the three-hold nim game.
    
    Vertical moves reduce the y-coordinate while keeping x constant,
    representing moves that take stones from the second pile.
    
    Parameters
    ----------
    x : int
        X-coordinate (first pile) of the current position.
    y : int
        Y-coordinate (second pile) of the current position.
        
    Returns
    -------
    set
        Set of encoded node indices representing all possible vertical moves.
    """
    vertical_next_node_set = set()

    while y > 0:
        y -= 1
        next_node = pairing_function(x, y)
        vertical_next_node_set.add(next_node)

    return vertical_next_node_set

def draw_horizon_edges(x, y):
    """
    Generate all possible horizontal moves from position (x, y) in the three-hold nim game.
    
    Horizontal moves reduce the x-coordinate while keeping y constant,
    representing moves that take stones from the first pile.
    
    Parameters
    ----------
    x : int
        X-coordinate (first pile) of the current position.
    y : int
        Y-coordinate (second pile) of the current position.
        
    Returns
    -------
    set
        Set of encoded node indices representing all possible horizontal moves.
    """
    horizon_next_node_set = set()

    while(x > 0):
        x -= 1
        next_node = pairing_function(x, y)
        horizon_next_node_set.add(next_node)

    return horizon_next_node_set

def draw_diagonal_edges(x, y):
    """
    Generate possible diagonal moves from position (x, y) in the three-hold nim game.
    
    Diagonal moves are only allowed when x + y = 3, representing special moves
    that take stones from both piles simultaneously with specific constraints.
    
    Parameters
    ----------
    x : int
        X-coordinate (first pile) of the current position.
    y : int
        Y-coordinate (second pile) of the current position.
        
    Returns
    -------
    set
        Set of encoded node indices representing all possible diagonal moves.
        Empty set if x + y != 3.
    """
    diagonal_next_node_set = set()

    if x + y != 3:
        return diagonal_next_node_set
    else:
        if x - 1 >= 0:
            next_node = pairing_function(x - 1, y + 1)
            diagonal_next_node_set.add(next_node)
        if y - 1 >= 0:
            next_node = pairing_function(x + 1, y - 1)
            diagonal_next_node_set.add(next_node)

    return diagonal_next_node_set

def draw_edges(x, y):
    """
    Generate all possible moves from position (x, y) in the three-hold nim game.
    
    This function combines vertical, horizontal, and diagonal moves to create
    the complete set of valid transitions from the current game state.
    
    Parameters
    ----------
    x : int
        X-coordinate (first pile) of the current position.
    y : int
        Y-coordinate (second pile) of the current position.
        
    Returns
    -------
    list
        List of encoded node indices representing all possible moves from (x, y).
    """
    # initialize sets
    next_node_set = set()
    vertical_next_node_set = draw_vertical_edges(x, y)
    horizon_next_node_set = draw_horizon_edges(x, y)
    diagonal_next_node_set = draw_diagonal_edges(x, y)

    # union all initialized sets
    next_node_set = next_node_set.union(
        vertical_next_node_set,
        horizon_next_node_set,
        diagonal_next_node_set
    )

    # convert set to list
    next_node_list = list(next_node_set)

    return next_node_list

def construct_three_hold_nim_graph(stone_num):
    """
    Construct the complete game graph for three-hold nim with specified number of stones.
    
    This function generates all possible game states and their transitions for a
    three-hold nim game, where states are represented as coordinates (x, y) with
    x + y ≤ stone_num, and encoded using the Cantor pairing function.
    
    Parameters
    ----------
    stone_num : int
        Maximum total number of stones in the game (x + y ≤ stone_num).
        
    Returns
    -------
    list
        List of adjacency lists representing the game graph, where each element
        contains the list of reachable states from the corresponding game position.
    """
    nodes = []

    for k in range(0, stone_num):
        for l in range(0, k + 1 ):
            x = l
            y = k - l
            node_adj = draw_edges(x, y)
            nodes.append(node_adj)

    return nodes


