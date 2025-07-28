import sys
import os

# Add parent directory to path to import adjacency_list
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from adjacency_list import GameGraph

def main():
    game_graph = GameGraph()
    file_path = input("Enter the path to the game graph file: ")

    try:
        game_graph.load_from_file(file_path)
        print(f"✅ Game graph loaded successfully with {game_graph.total_nodes} nodes.")
        
        # Display the adjacency list
        print("\nAdjacency List:")
        for index, adjacent_nodes in enumerate(game_graph.nodes):
            print(f"Node {index}: {', '.join(map(str, adjacent_nodes)) if adjacent_nodes else 'No adjacent nodes'}")

    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found.")
    except ValueError as e:
        print(f"❌ Error: Invalid file format - {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()