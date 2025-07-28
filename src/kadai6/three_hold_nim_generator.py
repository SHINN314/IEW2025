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

def draw_edges(nim, game_graph: GameGraph):
    for k in range(0, nim):
        x = 0
        y = k
        next_node_set = set()

        for l in range(0, k + 1):
            vertical_next_node_set = draw_vertical_edges(x, y)
            horizon_next_node_set = draw_horizon_edges(x, y)
            diagonal_next_node_set = draw_diagonal_edges(x, y)

            # union all sets
            next_node_set.union(vertical_next_node_set)
            next_node_set.union(horizon_next_node_set)
            next_node_set.union(diagonal_next_node_set)

            next_node_list = list(next_node_set) # convert set to list

            return next_node_list


