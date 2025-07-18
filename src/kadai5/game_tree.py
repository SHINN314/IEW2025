import collections
from node import Node
from parse_methods import GameParser, TreeVisualizer


class GameTree:
    def __init__(self):
        self.root_node = None

    def set_root_node(self, node):
        if not isinstance(node, Node):
            raise TypeError("Root node must be an instance of Node")
        self.root_node = node

    def parse_game(self, game_string):
        """
        ゲームの文字列表現を再帰的に解析し、Nodeオブジェクトの木構造を返す。
        """
        game_string = game_string.strip()

        # parse negation (-ゲーム)
        if game_string.startswith('-'):
            inner_game_string = game_string[1:].strip()
            inner_node = self.parse_game(inner_game_string)
            return GameParser.negate_game(inner_node, self.parse_game)

        # parse *k
        if game_string.startswith('*'):
            try:
                k = int(game_string[1:])
                return GameParser.create_recursive_nim_node(k, self.parse_game)
            except ValueError:
                raise ValueError(f"Invalid nim value format: '{game_string}'")
        
        # parse n × ↑ + *
        if '×' in game_string and '↑' in game_string and '+' in game_string and '*' in game_string:
            return GameParser.parse_n_times_up_plus_star(game_string, self.parse_game)
        
        # parse n × ↑
        if '×' in game_string and '↑' in game_string:
            return GameParser.parse_n_times_up(game_string, self.parse_game)
            
        # parse ↑
        if game_string == "↑":
            return GameParser.create_up_node(self.parse_game)
        
        # parse ↓
        if game_string == "↓":
            return GameParser.create_down_node(self.parse_game)

        # base case
        if game_string == "0":
            return Node("0")
        
        # parse positive integers
        if game_string.isdigit():
            n = int(game_string)
            return GameParser.create_integer_node(n, self.parse_game)
        
        # parse bracket notation { ... | ... }
        return GameParser.parse_bracket_notation(game_string, self.parse_game)

    def print_tree(self, node, prefix="", is_last=True, is_left=None):
        """
        木構造を可視化する関数（左の子と右の子を区別）
        """
        if node is None: 
            return
        
        # ノード名を表示（左/右の区別を追加）
        connector = "└── " if is_last else "├── "
        if is_left is None:
            # ルートノード
            print(f"{prefix}{connector}[ROOT] {node.name}")
        elif is_left:
            print(f"{prefix}{connector}[LEFT] {node.name}")
        else:
            print(f"{prefix}{connector}[RIGHT] {node.name}")
        
        # 子ノードの前置詞を決定
        new_prefix = prefix + ("    " if is_last else "│   ")
        
        # 左の子ノードを表示
        for i, left_child in enumerate(node.left_children):
            is_last_left = (i == len(node.left_children) - 1) and len(node.right_children) == 0
            self.print_tree(left_child, new_prefix, is_last_left, is_left=True)
        
        # 右の子ノードを表示
        for i, right_child in enumerate(node.right_children):
            is_last_right = (i == len(node.right_children) - 1)
            self.print_tree(right_child, new_prefix, is_last_right, is_left=False)
    
    def print_tree_enhanced(self):
        """改良された見やすい形式で木構造を表示"""
        if self.root_node is None:
            print("❌ No tree to display")
            return
        TreeVisualizer.print_tree_enhanced(self.root_node)
    
    def print_tree_compact(self):
        """コンパクトな形式で木構造を表示"""
        if self.root_node is None:
            print("❌ No tree to display")
            return
        TreeVisualizer.print_tree_compact(self.root_node)
    
    def generate_dot_graph(self, filename="game_tree", keep_dot=False):
        """DOT形式のグラフファイルを生成し、PNGに変換"""
        if self.root_node is None:
            print("❌ No tree to generate")
            return None
        return TreeVisualizer.generate_dot_graph(self.root_node, filename, keep_dot)
    
    def print_game_notation(self):
        """ゲーム記法で表示"""
        if self.root_node is None:
            print("❌ No tree to display")
            return
        TreeVisualizer.print_game_notation(self.root_node)
    
    def display_all_formats(self, filename="game_tree"):
        """すべての表示形式で木構造を出力"""
        if self.root_node is None:
            print("❌ No tree to display")
            return
        
        print("=" * 60)
        print("🌳 GAME TREE VISUALIZATION")
        print("=" * 60)
        
        print("\n1️⃣ ENHANCED TREE VIEW:")
        print("-" * 30)
        self.print_tree_enhanced()
        
        print("\n2️⃣ COMPACT TREE VIEW:")
        print("-" * 30)
        self.print_tree_compact()
        
        print("\n3️⃣ GAME NOTATION:")
        print("-" * 30)
        self.print_game_notation()
        
        print("\n4️⃣ GRAPH GENERATION:")
        print("-" * 30)
        self.generate_dot_graph(filename)
        
        print("\n" + "=" * 60)

