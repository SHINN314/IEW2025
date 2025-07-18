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

    def _parse_nim_value(self, k):
        """
        parse *k method
        *k = {*0,*1,...,*(k-1) | *0,*1,...,*(k-1)}
        *0 = 0 = { | }
        """
        if k == 0:
            # base case
            return Node("0")
        
        root = Node(f"*{k}")

        # left choices
        for i in range(k):
            left_child = self._parse_nim_value(i)
            root.add_left_child(left_child)

        # right choices
        for i in range(k):
            right_child = self._parse_nim_value(i)
            root.add_right_child(right_child)
        
        return root
    
    def _parse_up(self):
        root = Node("↑")

        left_chiled = Node("0")
        root.add_left_child(left_chiled)

        right_chiled = self._parse_nim_value(1)
        root.add_right_child(right_chiled)

        return root

    def _parse_sum_n_up_and_star(self, n):
        if n == 1:
            game_tree = "{0, * | 0}"
            root = self.parse_game(game_tree)
            return root

    def _parse_n_up(self, n):
        if n == 1:
            return self._parse_up()
        
    
    def _parse_down(self):
        root = Node("↓")

        left_chiled = self._parse_nim_value(1)
        root.add_left_child(left_chiled)

        right_chiled = Node("0")
        root.add_right_child(right_chiled)

        return root

    def _parse_n_up_times(self, game_string):
        """
        n × ↑ 形式をパースする
        n × ↑ = {0 | (n-1) × ↑ + *}
        """
        # "n × ↑" から n を抽出
        parts = game_string.split('×')
        if len(parts) != 2:
            raise ValueError(f"Invalid n × ↑ format: '{game_string}'")
        
        try:
            n = int(parts[0].strip())
        except ValueError:
            raise ValueError(f"Invalid number in n × ↑ format: '{parts[0].strip()}'")
        
        if n == 1:
            return self._parse_up()
        
        root = Node(f"{n} × ↑")
        
        # 左側: 0
        left_child = Node("0")
        root.add_left_child(left_child)
        
        # 右側: (n-1) × ↑ + *
        if n - 1 == 1:
            # 基底ケース: ↑ + * = {0, * | 0}
            right_child = self._parse_up_plus_star_base()
        else:
            right_child = self._parse_n_up_plus_star_from_n(n - 1)
        root.add_right_child(right_child)
        
        return root

    def _parse_n_up_plus_star(self, game_string):
        """
        n × ↑ + * 形式をパースする
        n × ↑ + * = {0 | (n - 1) × ↑}
        ↑ + * = {0, * | 0} (基底ケース)
        """
        # "n × ↑ + *" から n を抽出
        parts = game_string.split('×')
        if len(parts) != 2:
            raise ValueError(f"Invalid n × ↑ + * format: '{game_string}'")
        
        try:
            n = int(parts[0].strip())
        except ValueError:
            raise ValueError(f"Invalid number in n × ↑ + * format: '{parts[0].strip()}'")
        
        return self._parse_n_up_plus_star_from_n(n)

    def _parse_n_up_plus_star_from_n(self, n):
        """
        n × ↑ + * を数値 n から構築する
        """
        if n == 1:
            # 基底ケース: ↑ + * = {0, * | 0}
            return self._parse_up_plus_star_base()
        
        root = Node(f"{n} × ↑ + *")
        
        # 左側: 0
        left_child = Node("0")
        root.add_left_child(left_child)
        
        # 右側: (n - 1) × ↑
        if n - 1 == 1:
            right_child = self._parse_up()
        else:
            right_child = Node(f"{n - 1} × ↑")
            # (n - 1) × ↑ の子ノードを再帰的に構築
            temp_game_tree = GameTree()
            temp_node = temp_game_tree._parse_n_up_times(f"{n - 1} × ↑")
            right_child.left_children = temp_node.left_children
            right_child.right_children = temp_node.right_children
        root.add_right_child(right_child)
        
        return root

    def _parse_up_plus_star_base(self):
        """
        基底ケース: ↑ + * = {0, * | 0}
        """
        root = Node("↑ + *")
        
        # 左側: 0, *
        left_child_0 = Node("0")
        left_child_star = self._parse_nim_value(1)
        root.add_left_child(left_child_0)
        root.add_left_child(left_child_star)
        
        # 右側: 0
        right_child = Node("0")
        root.add_right_child(right_child)
        
        return root

    def parse_game(self, game_string):
        """
        ゲームの文字列表現を再帰的に解析し、Nodeオブジェクトの木構造を返す。
        """
        game_string = game_string.strip()

        # parse *k
        if game_string.startswith('*'):
            try:
                k = int(game_string[1:])
                return self._parse_nim_value(k)
            except ValueError:
                raise ValueError(f"Invalid nim value format: '{game_string}'")
        
        # parse n × ↑ + *
        if '×' in game_string and '↑' in game_string and '+' in game_string and '*' in game_string:
            return self._parse_n_up_plus_star(game_string)
        
        # parse n × ↑
        if '×' in game_string and '↑' in game_string:
            return self._parse_n_up_times(game_string)
            
        # parse ↑
        if game_string == "↑":
            return self._parse_up()
        
        # parse ↓
        if game_string == "↓":
            return self._parse_down()

        # base case
        if game_string == "0":
            return Node("0")
        if not game_string.startswith('{') or not game_string.endswith('}'):
            raise ValueError(f"Invalid game format: '{game_string}' does not start with '{{' or end with '}}'")

        # recurrent case
        root = Node(game_string)
        content = game_string[1:-1].strip()
        
        # if content == "":
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

