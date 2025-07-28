import sys
import os

# Add parent directory to path to import adjacency_list
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from adjacency_list import GameGraph
import roopy_grundy
import three_hold_nim_generator as nim_generator

def main():
    x, y = map(int, input("Input x and y of grid: ").split())

    # display node as integer
    node = nim_generator.pairing_function(x, y)
    print(f"node as integer: {node}")

    # calculate vertical next node set
    try:
        vertical_next_node_set = nim_generator.draw_vertical_edges(x, y)

        print(f"grid ({x}, {y})'s next node: {vertical_next_node_set}")
    except Exception as e:
        print(f"Drawing vertical next node set error: {e}")

    # calculate horizon next node set
    try:
        horizon_next_node_set = nim_generator.draw_horizon_edges(x, y)
        print(f"grid ({x}, {y})'s next node: {horizon_next_node_set}")
    except Exception as e:
        print(f"Drawing horizon next node set error: {e}")

    # calculate diagonal next node set
    try:
        diagonal_next_node_set = nim_generator.draw_diagonal_edges(x, y)
        print(f"grid ({x}, {y})'s next node: {diagonal_next_node_set}")
    except Exception as e:
        print(f"Drawing next node set error: {e}")

if __name__ == "__main__":
    main()