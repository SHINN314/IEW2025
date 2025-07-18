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
        print(f"✅ Root node set: {game_tree.root_node}")
        print("✅ Game tree parsed successfully.")
        
        # 表示形式の選択
        print("\nChoose display format:")
        print("1: Enhanced tree view")
        print("2: Compact tree view") 
        print("3: Game notation")
        print("4: Generate DOT graph")
        print("5: All formats")
        print("6: Original format")
        
        choice = input("Enter choice (1-6, default=5): ").strip()
        
        if choice == "1":
            game_tree.print_tree_enhanced()
        elif choice == "2":
            game_tree.print_tree_compact()
        elif choice == "3":
            game_tree.print_game_notation()
        elif choice == "4":
            filename = input("Enter filename (default=game_tree): ").strip() or "game_tree"
            keep_dot = input("Keep DOT file? (y/N): ").strip().lower() == 'y'
            game_tree.generate_dot_graph(filename, keep_dot)
        elif choice == "6":
            game_tree.print_tree(game_tree.root_node)
        else:  # choice == "5" or default
            filename = input("Enter filename for DOT graph (default=game_tree): ").strip() or "game_tree"
            game_tree.display_all_formats(filename)
            
    except ValueError as e:
        print(f"❌ Error parsing game tree: {e}")

if __name__ == "__main__":
    main()
