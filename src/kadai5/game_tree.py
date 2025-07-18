import collections
from node import Node

class GameTree:
    def __init__(self):
        self.root_node = None

    def set_root_node(self, node):
        if not isinstance(node, Node):
            raise TypeError("Root node must be an instance of Node")
        self.root_node = node

    @staticmethod
    def _split_options(options_str):
        """
        ネストされた括弧を考慮して、トップレベルの選択肢をカンマで分割するヘルパー関数。
        """
        options = []
        current_option = ""
        brace_level = 0
        options_str = options_str.strip()

        for char in options_str:
            if char == '{':
                brace_level += 1
            elif char == '}':
                brace_level -= 1
            elif char == ',' and brace_level == 0:
                # トップレベルのカンマで分割
                if current_option.strip():
                    options.append(current_option.strip())
                current_option = ""
                continue
                
            current_option += char
        
        # 最後の選択肢を追加
        if current_option.strip():
            options.append(current_option.strip())
            
        return options

    def parse_game(self, game_string):
        """
        ゲームの文字列表現を再帰的に解析し、Nodeオブジェクトの木構造を返す。
        """
        game_string = game_string.strip()
        print(f"Parsing game string: '{game_string}'")

        # base case
        if game_string == "0":
            return Node("{ | }")
        if not game_string.startswith('{') or not game_string.endswith('}'):
            raise ValueError(f"Invalid game format: '{game_string}' does not start with '{{' or end with '}}'")

        # recurrent case
        root = Node(game_string)
        content = game_string[1:-1].strip()
        
        # "|" がない場合 (例: "{ }") は空のゲームとして扱う
        if not content:
            return root

        brace_level = 0
        split_index = -1
        for i, char in enumerate(content):
            if char == '{':
                brace_level += 1
            elif char == '}':
                brace_level -= 1
            elif char == '|' and brace_level == 0:
                split_index = i
                break
                
        if split_index == -1:
            raise ValueError(f"Invalid game format: Separator '|' not found at top level in '{content}'")

        left_part_str = content[:split_index].strip()
        right_part_str = content[split_index + 1:].strip()
        
        if left_part_str:
            left_options = self._split_options(left_part_str)
            for option_str in left_options:
                child_node = self.parse_game(option_str)
                root.add_left_child(child_node)
            
        if right_part_str:
            right_options = self._split_options(right_part_str)
            for option_str in right_options:
                child_node = self.parse_game(option_str)
                root.add_right_child(child_node)

        return root


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

