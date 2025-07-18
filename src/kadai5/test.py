from game_tree import GameTree


def main():
    game_tree = GameTree()
    game_tree_text = input("Enter the game string: ")
    try:
        game_tree.set_root_node(game_tree.parse_game(game_tree_text))
        if game_tree.root_node is None:
            raise ValueError("Root node is not set. Please check the game string format.")
        print(f"Root node set: {game_tree.root_node}")
        print("Parsing game tree...")
        game_tree.parse_game(game_tree_text)
        print("Game tree parsed successfully.")
        game_tree.print_tree(game_tree.root_node)
    except ValueError as e:
        print(f"Error parsing game tree: {e}")

if __name__ == "__main__":
    main()
