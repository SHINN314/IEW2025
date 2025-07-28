from adjacency_list import GameGraph

def pairing_function(x, y):
    return (x + y) * (x + y + 1) // 2 + x

def draw_vertical_edges(x, y):
    vertical_next_node_set = set()

    while y > 0:
        y -= 1
        next_node = pairing_function(x, y)
        vertical_next_node_set.add(next_node)

    return vertical_next_node_set

def draw_horizon_edges(x, y):
    horizon_next_node_set = set()

    while(x > 0):
        x -= 1
        next_node = pairing_function(x, y)
        horizon_next_node_set.add(next_node)

    return horizon_next_node_set

def draw_diagonal_edges(x, y):
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
    nodes = []

    for k in range(0, stone_num):
        for l in range(0, k + 1):
            x = l
            y = k - l
            node_adj = draw_edges(x, y)
            nodes.append(node_adj)

    return nodes


