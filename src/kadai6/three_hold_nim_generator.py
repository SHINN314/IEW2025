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


def draw_edges(nim, game_graph: GameGraph):
    for k in range(0, nim):
        x = 0
        y = k
        next_node_set = set()

        for l in range(0, k + 1):
            vertical_next_node_set = draw_vertical_edges()
            horizon_next_node_set = draw_horizon_edges()
            diagonal_next_node_set = draw_diagonal_edges()

            # union all sets
            next_node_set.union(vertical_next_node_set)
            next_node_set.union(horizon_next_node_set)
            next_node_set.union(diagonal_next_node_set)

            next_node_list = list(next_node_set) # convert set to list

            return next_node_list


