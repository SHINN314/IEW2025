from game_tree import GameTree
from parse_methods import GameParser

def test_sum_n_up_and_star():
    game_tree = GameTree()
    # 直接括弧記法でパースする
    result = game_tree.parse_game("{0, *1 | 0}")
    game_tree.set_root_node(result)
    game_tree.print_tree(game_tree.root_node)


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
