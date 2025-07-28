import sys
import os

# Add parent directory to path to import adjacency_list
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from adjacency_list import GameGraph
import roopy_grundy
import three_hold_nim_generator as nim_generator

def main():
    x, y = map(int, input("Initialize x and y. Please input like 'x y': ").split())
    node = nim_generator.pairing_function(x, y)
    game_graph = GameGraph()

    # calculate next node list
    try:
        node_adj = nim_generator.draw_edges(x, y)
        print(f"Node {node}: Adjacency list {node_adj}")
    except Exception as e:
        print(e)

    # construct three hold nim game graph
    try:
        stone_num = int(input("Choose initialize stone of three hold nim game: "))
        nodes = nim_generator.construct_three_hold_nim_graph(stone_num)

        for node, node_adj in enumerate(nodes):
            print(f"Node {node}: Adfacency list {node_adj}")

    except Exception as e:
        print(f"Constructing three hold nim game graph: {e}")

if __name__ == "__main__":
    main()