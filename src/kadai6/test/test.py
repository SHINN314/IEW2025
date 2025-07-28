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
        nodes = nim_generator.draw_edges(x, y)
        print(f"Node {node}: Adjacency list {nodes}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()