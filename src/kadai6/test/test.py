import sys
import os

# Add parent directory to path to import adjacency_list
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from adjacency_list import GameGraph
import roopy_grundy

def main():
    game_graph = GameGraph()
    file_path = input("Enter the path to the game graph file: ")

    # load file
    try:
        game_graph.load_from_file(file_path)
        print(f"✅ Game graph loaded successfully with {game_graph.total_nodes} nodes.")

    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found.")
    except ValueError as e:
        print(f"❌ Error: Invalid file format - {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

    # initialize Grundy numbers
    try:
        grundy_numbers = roopy_grundy.initialize_grundy_numbers(game_graph)

        # display initialized Grundy numbers
        print("✅ Grundy numbers initialized:")
        for node_id, grundy_number in enumerate(grundy_numbers):
            print(f"Node {node_id}: Grundy number = {grundy_number}")

    except Exception as e:
        print(f"❌ Error initializing Grundy numbers: {e}")

if __name__ == "__main__":
    main()